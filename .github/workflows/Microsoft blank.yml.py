# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "main" branch
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: Run a multi-line script
        run: |
          echo Add other actions to build,
          echo test, and deploy your project.
name: AutoBuild
on:
  push:
    branches: [ OneKeyVip-master ]
  pull_request:
    branches: [ OneKeyVip-master ]
jobs:
  build:
    name: build
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: npm install
      run: |
        npm install
        npm ci
    - name: npm build
      run: |
       npm run build
       cp README.MD ./publish/README.MD
       cp CHANGELOG ./publish/CHANGELOG
    - name: publish
      uses: s0/git-publish-subdir-action@master
      env:
        REPO: 目标库
        BRANCH: 目标分支
        FOLDER: 要发布的内容所在的文件夹
        SSH_PRIVATE_KEY: ${{ secrets.publish }}
