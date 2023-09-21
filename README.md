# Qwen-Agent
[中文](./README_CN.md) ｜ English

Qwen-Agent is a code library based on LLM that integrates components such as plugin usage, planning generation, and action execution. At present, we have implemented a Google Extension ```GhostWriter``` to facilitate your knowledge integration and content editing work. The features of ghostwriter include:

- It can record your webpage browsing content with your permission, and use Qwen (abbr. Tongyi Qianwen) as an analysis assistant to assist you in completing editing work based on the browsing content. Through it, you can quickly complete tedious tasks such as understanding web content, organizing browsing content, and writing new articles.
- Supporting the analysis of open PDF documents (Online or local). You can open PDF documents in a browser and quickly talk about them with Qwen.
- Supporting plugin calls, and currently integrating plugins such as Code Interpreter and Google Search.

# Demonstration
## Q&A in Browser Interactive Interface

<div style="display:flex;">
    <figure style="width:45%;">
        <img src="assets/screenshot-pdf-qa.png" alt="paper-attention-qa">
        <figcaption style="text-align:center;">Question Answering over a PDF</figcaption>
    </figure>
    <figure style="width:45%;">
        <img src="assets/screenshot-web-qa.png" alt="paper-attention-qa">
        <figcaption style="text-align:center;">Question Answering over a Webpage</figcaption>
    </figure>
</div>

## Editing Workstation
<div style="display:flex;">
    <figure>
        <img src="assets/screenshot-writing.png" alt="paper-attention-qa">
        <figcaption style="text-align:center;">Writing Articles based on Browsed Webpages and PDFs</figcaption>
    </figure>
    <figure>
        <img src="assets/screenshot-editor-movie.png" alt="paper-attention-qa">
        <figcaption style="text-align:center;">Calling Plugins to Assist in Writing</figcaption>
    </figure>
</div>

<div style="display:flex;">
    <figure>
        <img src="assets/screenshot-multi-web-qa.png" alt="paper-attention-qa">
        <figcaption style="text-align:center;">Question Answering over Multiple Webpages</figcaption>
    </figure>
    <figure>
        <img src="assets/screenshot-ci.png" alt="paper-attention-qa">
        <figcaption style="text-align:center;">Ask Qwen to draw Figures by Code Interpreter</figcaption>
    </figure>
</div>

# How to use Ghostwriter

## Quick Start
```
git clone https://github.com/QwenLM/Qwen-Agent.git
cd Qwen-Agent
pip install -r requirements.txt
```

## Configuration
- Setting necessary parameters in ```configs/config_ghostwriter. py```, commonly used parameters are as follows:
    - llm: The large model. Now supporting OpenAI API format, default to ```Qwen-7B-Chat```
    - MAX_TOKEN：The maximum number of tokens for reference materials, default to ```5000```
    - fast_api_host、app_host、app_in_browser_host：The address and port of the backend service, default to ```127.0.0.1```

## Start Service
### Start Qwen: Refer to the OpenAI API deployment method in [Qwen-7B](https://github.com/QwenLM/Qwen-7B/blob/main/README.md#api):

```
python openai_api.py --server-port 8003
```
- After deploying Qwen, modify ```openai.api_base``` in ```agent/llm/qwen.py``` to the corresponding address and port, default to "http://localhost:8003/v1"

### Start the Backend Services of Google Extension and Editing Workstation:
```
cd qwen_agent/ghostwriter/server
python run_server.py
```
- Pressing ```Ctrl+C``` can close the service
- Note: After modifying the configuration file or code, the service need to be restarted to take effect


### Upload to Google Extension
- Entering [Google Extension](chrome://extensions/)
- Finding file ```ghostwriter``` in ```Qwen-Agent/qwen_agent/```, uploading and enabling
- Clicking on the Google Chrome Extensions icon in the top right corner of Google Chrome to pin ghostwriter in the toolbar

### Usage Tips
- When you find browsing web content useful, click the ```Add to Qwen's Reading List``` button in the upper right corner of the screen, and Qwen will analyze this page in the background. (Considering user privacy, user must first click on the button to authorize Qwen before reading this page)
- Clicking on the Qwen icon in the upper right corner to communicate with Qwen on the current browsing page.
- Accessing the default address```http://127.0.0.1:7864/``` to work on the editing workstation and Qwen will assist you with editing based on browsing records.

- The editing workstation is shown in the following figure, mainly consisting of five areas:
    - Start Date/End Date: Selecting the browsed materials for the desired time period, including the start and end dates
    - Browser List: The browsed materials list, supporting the selection or removal of specific browsing content and supporting for manually adding URLs to browsing lists
    - Recommended Topics: Qwen generates recommended topics based on browsed materials, supporting regeneration
    - Editor: In the editing area, you can directly input content or special instructions, and then click the ```Continue``` button to have Qwen assist in completing the editing work:
        - After inputting the content, directly click the ```Continue``` button: Qwen will begin to continue writing based on the browsing information
        - Using special instructions:
            - /title + content: Qwen enables the built-in planning process and writes a complete manuscript
            - /code + content: Qwen enables the code interpreter plugin, writes and runs Python code, and generates replies
            - /plug + content: Qwen enables plugin and select appropriate plugin to generate reply
    - Chat: Interactive area. Qwen generates replies based on given reference materials. Selecting CI will enable the code interpreter plugin, which supports uploading files for data analysis

# Code structure

- qwen_agent
    - agents: The implementation of general methods for planning/tools/actions/memory
    - llm: Defining the interface for accessing LLM, currently providing OpenAI format access interface for Qwen-7B
    - ghostwriter: The implementation of ghostwriter, including google extension configuration, front-end interface, and backend processing logic
    - configs: Storing the configuration files where you can modify local service ports and other configurations