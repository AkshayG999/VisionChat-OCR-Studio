# Ollama Command Line Interface (CLI) Documentation

## Overview

`ollama` is a tool used for managing and interacting with large language models (LLMs). It offers several commands to manage models, run them, and interact with them.

## Commands

### `ollama serve`
Starts the Ollama server.

**Usage:**
```bash
ollama serve
```

**Error Handling:**
- If you get an error like `listen tcp 127.0.0.1:11434: bind: address already in use`, it indicates the port is already in use. Ensure no other process is using the same port.

### `ollama pull <model-name>`
Pulls a model from a registry.

**Usage:**
```bash
ollama pull <model-name>
```

**Example:**
```bash
ollama pull llama3.2-vision:11b
```

This command downloads a model, such as `llama3.2-vision:11b`, from the registry. It pulls the model components and verifies the integrity via SHA256 digest.

### `ollama list`
Lists all available models on the local system.

**Usage:**
```bash
ollama list
```

**Example output:**
```
NAME                      ID              SIZE      MODIFIED       
llama3.2-vision:latest    085a1fdae525    7.9 GB    9 seconds ago     
llama3.2-vision:11b       085a1fdae525    7.9 GB    16 minutes ago    
```

### `ollama run <model-name>`
Runs a model with optional inputs.

**Usage:**
```bash
ollama run <model-name> [flags]
```

**Example:**
```bash
ollama run llama3.2-vision --input "Hello, how are you?"
```

**Note:** The flag `--input` may not be available, as shown in the example `Error: unknown flag: --input`. Refer to the `ollama --help` for the correct flags for each command.

### `ollama show <model-name>`
Shows detailed information about a model.

**Usage:**
```bash
ollama show <model-name>
```

**Example:**
```bash
ollama show llama3.2-vision
```

**Example output:**
```
Model
  architecture        mllama    
  parameters          9.8B      
  context length      131072    
  embedding length    4096      
  quantization        Q4_K_M    

Projector
  architecture        mllama     
  parameters          895.03M    
  embedding length    1280       
  dimensions          4096       

Parameters
  temperature    0.6    
  top_p          0.9    

License
  LLAMA 3.2 COMMUNITY LICENSE AGREEMENT                 
  Llama 3.2 Version Release Date: September 25, 2024    
```

### `ollama ps`
Shows the status of running models.

**Usage:**
```bash
ollama ps
```

**Example output:**
```
NAME                      ID              SIZE      PROCESSOR    UNTIL              
llama3.2-vision:latest    085a1fdae525    12 GB    100% CPU     3 minutes from now    
```

### `ollama chat`
Starts an interactive chat session with the model (if available).

**Usage:**
```bash
ollama chat <model-name>
```

**Example:**
```bash
ollama chat llama3.2-vision
```

**Error Handling:**
- If you get an error like `Error: unknown command "chat" for "ollama"`, the command may not be supported in the installed version.

## General Flags

### `-h`, `--help`
Displays help information for any command.

**Usage:**
```bash
ollama --help
```

**Example output:**
```
Large language model runner

Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command
```

### `--version`
Shows the version of `ollama` installed.

**Usage:**
```bash
ollama --version
```

**Example output:**
```
ollama version is 0.5.7
```

## License
The `ollama` tool and models are subject to the LLAMA 3.2 COMMUNITY LICENSE AGREEMENT. Refer to the documentation for more details.