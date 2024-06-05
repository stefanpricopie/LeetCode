import re
import requests
import plotly.express as px
import pandas as pd
import time

GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "stefanpricopie"
REPO_NAME = "LeetCode"

# TODO: Add GITHUB_ACCESS_TOKEN to your environment variables

# Function to check for rate limit errors
def check_rate_limit(response):
    if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
        if int(response.headers['X-RateLimit-Remaining']) == 0:
            reset_time = int(response.headers['X-RateLimit-Reset'])
            raise Exception(f"Rate limit exceeded. Try again after {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reset_time))}.")
    response.raise_for_status()

# Function to get all .py files from the repository
def get_py_files(repo_owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/git/trees/main?recursive=1"
    response = requests.get(url)
    check_rate_limit(response)
    tree = response.json().get('tree', [])
    return [file['path'] for file in tree if file['path'].endswith('.py')]

# Function to get the latest commit message for a file
def get_latest_commit_message(repo_owner, repo_name, file_path):
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/commits"
    params = {'path': file_path, 'per_page': 1}
    response = requests.get(url, params=params)
    check_rate_limit(response)
    commits = response.json()
    if commits:
        return commits[0]['commit']['message']
    return None

# Function to parse performance metrics from commit messages
def parse_metrics(commit_message):
    pattern = re.compile(r"Time: .*? \((\d+\.\d+)%\), Space: .*? \((\d+\.\d+)%\)")
    match = pattern.search(commit_message)
    if match:
        time, space = match.groups()
        return {'time': float(time), 'space': float(space)}
    return None

# Function to extract problem number from file path
def extract_problem_number(file_path):
    match = re.search(r'/(\d{4})-', file_path)
    if match:
        return str(int(match.group(1)))  # Convert to int to drop leading zeros and back to string
    return "Unknown"

# Function to create and save an interactive plot
def create_and_save_plot(data, save=True):
    df = pd.DataFrame(data)
    fig = px.scatter(df, x='time', y='space', text='problem', title='Python Solutions Compared to other Users')
    fig.update_traces(textposition='top center')
    fig.update_layout(
        yaxis=dict(
            scaleanchor="x", 
            scaleratio=1, 
            range=[0, 105],
            title='Beats %Users on Space'  # Set y-axis label
        ),
        xaxis=dict(
            range=[0, 100],
            title='Beats %Users on Time'  # Set x-axis label
        ),
        width=600,  # Set figure width to enforce a square layout
        height=600  # Set figure height to enforce a square layout
    )
    if save:
        fig.write_html("algorithm_performance.html", include_plotlyjs='cdn')
        fig.write_image("algorithm_performance.png", scale=2)
    return fig

# Main function
def main():
    try:
        py_files = get_py_files(REPO_OWNER, REPO_NAME)
    except Exception as e:
        print(e)
        return

    data = []
    for file_path in py_files:
        try:
            commit_message = get_latest_commit_message(REPO_OWNER, REPO_NAME, file_path)
            if commit_message:
                metrics = parse_metrics(commit_message)
                if metrics:
                    metrics['file'] = file_path
                    metrics['problem'] = extract_problem_number(file_path)
                    data.append(metrics)
        except Exception as e:
            print(e)
            continue

    if data:
        fig = create_and_save_plot(data)
        fig.show()
    else:
        print("No performance metrics found in commit messages.")
    
    return data

if __name__ == "__main__":
    data = main()