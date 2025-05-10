import os
import subprocess
import webbrowser
import time

# Function to run the generate_tests.py script
def generate_tests():
    print("🔄 Generating tests...")
    subprocess.run(["python", "./generate_tests.py"], check=True)
    print("✅ Tests generated successfully!")

# Function to run pytest and generate test report
def run_tests():
    print("🔄 Running tests with pytest...")
    result = subprocess.run(["pytest", "-v", "test_routes.py"], capture_output=True, text=True)
    print(result.stdout)  # Display pytest output
    # Save the test report to an HTML file
    subprocess.run(["pytest", "--disable-warnings", "--html=report.html"], check=False)
    print("✅ Test report generated: report.html")

# Function to open the test report in the default browser
def open_test_report():
    print("🔄 Opening test report...")
    time.sleep(1)  # Wait for the report to be generated
    webbrowser.open("report.html")
    print("✅ Test report opened in browser.")

# Function to run pytest with coverage
def run_coverage():
    print("🔄 Running tests with coverage...")
    result = subprocess.run(["pytest", "--cov=app", "--cov-report=term", "--cov-report=html", "test_routes.py"], capture_output=True, text=True)
    print(result.stdout)  # Display coverage output
    print("✅ Coverage report generated!")

import os

def open_coverage_report():
    print("🔄 Opening coverage report...")
    time.sleep(1)  # Wait for the report to be generated
    coverage_report_path = "htmlcov/index.html"
    
    # Check if the coverage report exists
    if os.path.exists(coverage_report_path):
        webbrowser.open("file:///" + os.path.abspath(coverage_report_path))
        print("✅ Coverage report opened in browser.")
    else:
        print(f"❌ Coverage report not found at {coverage_report_path}. Please ensure the tests have run with coverage.")



# Main function to run the complete job
def main():
    # Step 1: Generate tests
    generate_tests()

    # Step 2: Run tests and generate test report
    run_tests()

    # Open test report
    open_test_report()

    # Step 3: Run tests with coverage
    run_coverage()

    if not os.getenv("CI"):  # GitHub Actions sets CI=true
        open_test_report()

if __name__ == "__main__":
    main()
