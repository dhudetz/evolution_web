# Overview
The purpose of this repo is to create a web-based, efficient, and user-friendly evolution simulation in the browser. Hoping to utilize WASM and WebGPU through Rust for efficient resource utilization.

# Usage

### Setup
1. [Install Node.js](https://nodejs.org/en/download)
2. `npm install http-server`

### How to build and run
From the root directory of the repo:
1. Build the WASM package with the build script: `python build.py`
2. Start the web server: `http-server .`


## Inspiration
* [WebGPU demos - wireframes](https://webgpu.github.io/webgpu-samples/?sample=wireframe)
* [BEVY WebGPU demos](https://bevyengine.org/examples-webgpu/)
    * [Low poly fox animation](https://bevyengine.org/examples-webgpu/animation/animation-graph/)
    * [Spatial audio](https://bevyengine.org/examples-webgpu/audio/spatial-audio-2d/)

## Supporting Technologies
* [Rust api to WebGPU in browser](https://github.com/gfx-rs/wgpu)
* [SpacetimeDB](https://spacetimedb.com/)
* [WASM Starter Tutorial](https://www.youtube.com/watch?v=hcA_GuZHyZM)

