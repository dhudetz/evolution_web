#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys

RUST_FOLDER = "wasm-test/"

def run_command(command, error_message):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {error_message}")
        print(e.stderr)
        sys.exit(1)

def main():
    # Ensure wasm-pack is installed
    print("Checking for wasm-pack...")
    if shutil.which("wasm-pack") is None:
        print("Error: wasm-pack is not installed. Installing it now...")
        run_command("cargo install wasm-pack", "Failed to install wasm-pack.")
    else:
        print("wasm-pack is installed.")

    # Check for Cargo.toml in current directory or RUST_FOLDER/
    project_dir = None
    if os.path.isfile("Cargo.toml"):
        project_dir = "."
        print("Found Cargo.toml in current directory.")
    elif os.path.isfile(os.path.join(RUST_FOLDER, "Cargo.toml")):
        project_dir = RUST_FOLDER
        print(f"Found Cargo.toml in {RUST_FOLDER} directory.")
    else:
        print(f"Error: Cargo.toml not found in current directory or {RUST_FOLDER}. Please ensure you're in a Rust project directory.")
        sys.exit(1)

    # Change to the project directory if necessary
    original_dir = os.getcwd()
    if project_dir != ".":
        print(f"Changing to {project_dir}/ directory...")
        os.chdir(project_dir)

    try:
        # Clean previous build artifacts (optional)
        print("Cleaning previous build artifacts...")
        if os.path.exists("pkg"):
            shutil.rmtree("pkg")

        # Build the project for WebAssembly (target: web)
        print("Building Rust project to WebAssembly...")
        run_command("wasm-pack build --target web", "Build failed. Please check the output for details.")

        print("Build successful! WebAssembly files are in the 'pkg/' directory.")
    finally:
        # Change back to the original directory
        os.chdir(original_dir)

if __name__ == "__main__":
    main()