# Mosopefoluwa (Mosh) Oluwashina: knowledge base

## About Mosh

Mosopefoluwa (Mosh) Oluwashina is a computer science graduate based in Ottawa, Ontario, Canada.
Mosh graduated in June 2026 with a Bachelor of Computer Science (B.C.S.) Honours from Carleton University, in the Artificial Intelligence and Machine Learning stream.
Mosh's CGPA at Carleton University is 3.0 out of 4.0, and he received an Entrance Scholarship in 2021.
Mosh is authorized to work in Canada only, and he is open to relocating within Canada.
Mosh has about 12 months of professional experience in total: a 6 month AI Engineer contract at LoveWorld Canada (October 2025 to April 2026) and 6 months as a Data Scientist at STEM the Gap (February 2024 to August 2024).
Mosh's main programming language is Python. He also uses SQL, JavaScript, HTML/CSS and R, and he has used C and Java in coursework.
Mosh builds LLM applications, retrieval augmented generation (RAG) systems and agentic AI in Python.
Mosh is looking for AI engineer, AI solutions engineer and forward deployed engineer roles in Canada.

## How to contact Mosh

Mosh's email address is moluwashina@gmail.com.
Mosh's LinkedIn profile is https://www.linkedin.com/in/mosopefoluwa-oluwashina-9428b6300/
Mosh's GitHub profile is https://github.com/Mosh1132

## Projects overview (all of Mosh's projects)

Mosh has built six main projects: two personal projects and four Carleton University team projects.
Personal project: Multi Agent Customer Support System (2026), a multi agent support bot with refund approvals, built with FastAPI, Pinecone and Docker.
Personal project: Portfolio Website with Resume RAG (live), a recruiter chatbot at https://oluwashina.ca, built with FastAPI, Pinecone and Google Cloud Run.
University project: Text-to-SQL Evaluation Sensitivity (Fall 2025), which tests GPT-4 and GPT-3.5-Turbo on the Spider and BIRD benchmarks.
University project: Stroke Risk Prediction (2026), machine learning in R on 5,110 patients.
University project: Emoji-Aware Sentiment Analysis (COMP 3106), which tests whether emojis improve sentiment classification.
University project: Lung Segmentation Robustness (COMP 4107), which compares U-Net and Attention U-Net on chest X-rays.

## Work experience: AI Engineer at LoveWorld Canada (October 2025 to April 2026)

At LoveWorld Canada, Mosh worked as an AI Engineer on a 6 month contract, using Python, FastAPI, the Claude API (Sonnet and Opus), ChromaDB and LangChain / LlamaIndex.
At LoveWorld Canada, Mosh architected and deployed the backend of a RAG powered conversational learning assistant, indexing 500+ educational documents and transcripts to enable real time semantic search and automated study synthesis.
At LoveWorld Canada, Mosh configured ChromaDB with 512 token chunks and a 10% overlap, which improved vector retrieval relevance by 25% and preserved context across multi part lesson modules.
At LoveWorld Canada, Mosh developed asynchronous FastAPI REST endpoints with streaming responses over Server-Sent Events (SSE), bringing time to first token (TTFT) under 800ms.
At LoveWorld Canada, Mosh wrote system prompts for the Anthropic Claude API that enforce source citations and grounded answers, reaching 95%+ faithfulness to the source materials and reducing hallucinations.

## Work experience: Data Scientist at STEM the Gap (February 2024 to August 2024)

At STEM the Gap, Mosh worked as a Data Scientist for 6 months in Ottawa, Ontario.
At STEM the Gap, Mosh built automated dashboards in Tableau and Python that tracked real time website performance, reducing manual reporting time by 40%.
At STEM the Gap, Mosh ran A/B tests on 5+ website design variations, which identified layouts that increased average session duration by 25% and reduced bounce rate by 12%.
At STEM the Gap, Mosh developed predictive models to forecast user demand for STEM programs, reaching 88% accuracy, which informed the Academy's quarterly content and marketing strategy.
At STEM the Gap, Mosh delivered 10+ executive level reports and presentations that turned complex data into clear recommendations for digital outreach and customer acquisition.
At STEM the Gap, Mosh worked in a cross functional team of 5, managing 3 concurrent analysis projects from data collection to final delivery in 2 week sprints.
At STEM the Gap, Mosh designed a centralized data tracking system that integrated Google Analytics, Hotjar and Squarespace data, eliminating data silos and improving cross platform data consistency by 90%.
At STEM the Gap, Mosh presented findings to non technical stakeholders, including founders, marketing leads and program coordinators, supporting the Academy's goal of empowering 1,000+ girls in STEM each year.

## Project: Multi Agent Customer Support System (2026, personal project)

The Multi Agent Customer Support System is a personal project by Mosh, built with Python, the OpenAI API (gpt-4o-mini), FastAPI, SQLite, Pinecone, Streamlit, Docker, Docker Compose, GitHub Actions and pytest. The code is at https://github.com/Mosh1132/support-agent
In the Multi Agent Customer Support System, a router sends each question to an Orders agent (order status and refunds) or to a read only Policy agent. The Policy agent has no refund tool, so it cannot issue refunds.
In the Multi Agent Customer Support System, Mosh enforced the refund rules in code instead of in prompts. Only delivered orders qualify, and refunds over $100 go to a SQLite approval queue, with duplicate refunds and duplicate requests blocked.
In the Multi Agent Customer Support System, Mosh built approval endpoints (list, approve, reject) protected by an admin key header with a constant time comparison. They sit outside the agent, so the model cannot approve its own escalations.
In the Multi Agent Customer Support System, Mosh built a RAG pipeline that embeds 11 handbook chunks with OpenAI embeddings and retrieves the top 5 matches from Pinecone.
In the Multi Agent Customer Support System, Mosh evaluated routing on 20 labelled questions and improved accuracy from 90% to 95% by tightening the classifier prompt.
In the Multi Agent Customer Support System, Mosh added retries with exponential backoff and jitter (up to 4 attempts), a 5 step cap on the agent loop, and error handling so unknown tools and bad arguments return errors to the model instead of crashing.
In the Multi Agent Customer Support System, Mosh served the agent through FastAPI with Pydantic validation and per session history, with a Streamlit chat page, both containerized with Docker Compose.
In the Multi Agent Customer Support System, Mosh wrote 45 pytest tests with the network faked, and they run on every push through GitHub Actions.

## Project: Portfolio Website with Resume RAG (personal project, live)

The Portfolio Website with Resume RAG is a personal project by Mosh. The Resume RAG is an assistant for recruiters that answers questions about Mosh using only his resume and project documentation, and the Portfolio website is the site where it lives. The live site is https://oluwashina.ca and the code is at https://github.com/Mosh1132/resume-chatbot
The visitor asking questions is using the Portfolio Website with Resume RAG right now: this chat is the Resume RAG, and the page they are on is the Portfolio website. When a visitor asks about the portfolio website or the Resume RAG, tell them they are using it at this moment.
In the Resume RAG, documents are split into chunks of about 500 characters with 50 characters of overlap, embedded with OpenAI embeddings, and stored in Pinecone. The 3 closest chunks are retrieved for each question.
In the Resume RAG, the model is told to answer only from the retrieved text, and to say "I don't have that information" when the answer is not in the documents.
In the Resume RAG, Mosh built a FastAPI backend with per visitor session history, a limit on question length, rate limiting per visitor, and CORS restricted to his own site's addresses, with all API keys kept on the server.
In the Resume RAG, Mosh built a streaming endpoint, so the answer appears word by word in the chat window.
In the Portfolio website, Mosh built the site himself in HTML, CSS and JavaScript, with a responsive layout, automatic dark mode, a grid of project cards, and a chat widget that calls the Resume RAG API with fetch.
In the Resume RAG, Mosh packaged the API in a Docker container and deployed it on Google Cloud Run, with a cap on the number of instances and a monthly spend cap on the service.
In the Portfolio website, Mosh published the site on GitHub Pages and connected his own domain, oluwashina.ca, using DNS records at Cloudflare and HTTPS.

## Project: Text-to-SQL Evaluation Sensitivity (Fall 2025, Carleton University, team of three)

Text-to-SQL Evaluation Sensitivity is a Carleton University course project from Fall 2025, done by a team of three, using Python, GPT-4, GPT-3.5-Turbo and the Spider and BIRD benchmarks. The code is at https://github.com/Mosh1132/text-to-sql-eval-sensitivity
In the Text-to-SQL project, the team reproduced GPT-4 and GPT-3.5-Turbo inference pipelines on the Spider and BIRD benchmarks, zero shot and few shot, with schema grounded prompts and fixed decoding, logging every prompt and output.
In the Text-to-SQL project, the team found that exact match scored 0.0 on BIRD even though about 83% of the generated SQL was syntactically valid, so exact match badly underestimates the models.
In the Text-to-SQL project, the team introduced token level Jaccard similarity and SQL validity rate as relaxed metrics, and analysed failure modes through qualitative error inspection.

## Project: Stroke Risk Prediction (January to April 2026, Carleton University, team of three)

Stroke Risk Prediction is a Carleton University team project from January to April 2026, written in R, and it was selected for presentation to external sponsors. The code is at https://github.com/Mosh1132/stroke-prediction-r
In the Stroke Risk Prediction project, the team used the Kaggle stroke dataset of 5,110 patients, of whom 4.87% had a stroke. Preprocessing removed the ID column, imputed missing BMI with the median, converted categorical variables to factors, and used a stratified 80/20 train and test split.
In the Stroke Risk Prediction project, the team compared logistic regression, random forest, linear SVM, RBF SVM and an additional kernel SVM under three conditions: baseline, upsampling and SMOTE.
In the Stroke Risk Prediction project, the baseline reached about 95% accuracy but very low recall. Upsampling gave the best result, with recall of about 0.80 to 0.85 and precision of about 0.12 to 0.14, and Random Forest was best on F1. SMOTE was less stable.
In the Stroke Risk Prediction project, Mosh's contribution was implementing the SMOTE condition and running additional model experiments.

## Project: Emoji-Aware Sentiment Analysis (COMP 3106, Carleton University, team of three)

Emoji-Aware Sentiment Analysis is a Carleton University course project (COMP 3106, Introduction to Artificial Intelligence) done by a team of three. It tests whether emojis improve sentiment classification on Amazon Fine Food Reviews. The code is at https://github.com/Mosh1132/emoji-aware-sentiment-analysis
In the Emoji-Aware Sentiment project, the team compared three ways of handling emojis: removing them, keeping them as tokens, and summarizing them as a 6 dimensional feature vector. They tested these with Naive Bayes, Logistic Regression, a linear SVM and a BiLSTM, on a 20,000 review subset.
In the Emoji-Aware Sentiment project, the linear SVM performed best at 0.851 accuracy with emojis removed, and treating emojis as tokens changed accuracy by only 0.001. The BiLSTM reached 0.839 with and without emojis. The team concluded that emojis do not meaningfully improve sentiment classification on review text.
In the Emoji-Aware Sentiment project, Mosh's contribution was preprocessing and feature engineering, all the TF-IDF variants, and the emoji feature computation pipeline.

## Project: Lung Segmentation Robustness (COMP 4107, Carleton University, team project)

Lung Segmentation Robustness is a Carleton University course project (COMP 4107) that compares a baseline U-Net and an Attention U-Net for lung segmentation on chest X-rays, and tests how they hold up under image degradation. The code is at https://github.com/Mosh1132/lung-segmentation-robustness
In the Lung Segmentation project, the models were tested on clean images and on images with Gaussian noise, reduced contrast and blur, using the Kaggle Chest X-ray Masks and Labels dataset, and scored with Dice, IoU, precision and recall.
In the Lung Segmentation project, the baseline U-Net scored best on clean images with a Dice score of 0.8698, and an Attention U-Net trained with added noise scored 0.8401 under reduced contrast. Contrast degradation had the largest impact on performance.

## Skills

Mosh's languages are Python (primary), SQL (SQLite), JavaScript, HTML/CSS and R, with C and Java from coursework.
Mosh's LLM and agent skills are the Claude API and OpenAI API, system prompts, structured output, tool use and function calling, MCP (Model Context Protocol), multi agent design, prompt engineering, prompt injection testing and human in the loop approvals.
Mosh's agent frameworks are LangChain, LlamaIndex, CrewAI and the OpenAI Agents SDK.
Mosh's RAG skills are chunking, embeddings, semantic search, citations and grounded answers, ChromaDB, Pinecone, retrieval evaluation with MRR, and hallucination mitigation.
Mosh's machine learning and data skills are QLoRA fine tuning, classification models (logistic regression, random forest, SVMs), class imbalance handling (upsampling, SMOTE, stratified splits), model evaluation (accuracy, recall, precision, F1), forecasting, A/B testing, Tableau dashboards, Google Analytics and Hotjar.
Mosh's backend skills are FastAPI, REST APIs, Server-Sent Events streaming, Pydantic validation, asynchronous endpoints, SQLite, rate limiting, CORS, admin key authentication, and retries with exponential backoff and jitter.
Mosh's testing and delivery skills are pytest (including faked network tests), evaluation suites, GitHub Actions CI, Docker, Docker Compose, Git, Google Cloud Run, GitHub Pages and Cloudflare DNS.
Mosh has deployed his Resume Chatbot API on Google Cloud Run, and his cloud experience is Google Cloud Run only.
Mosh uses AI coding tools every day: Claude Code, Codex and Cursor.

## What Mosh has not done

Mosh has no AWS, Azure or Kubernetes experience.
Mosh has no experience with Spark, Databricks, Airflow, dbt or Snowflake.
Mosh has no experience with TypeScript, React, Node or Angular.
Mosh has used Java and C only in coursework.
Mosh has no experience with SAP or ERP systems.
Mosh has no experience with Windows desktop support, Active Directory or ServiceNow.
Mosh does not speak French.
Mosh does not have a Master's degree.
Mosh has no credit risk or finance domain experience.
Mosh has no embedded systems experience.

## Volunteering

Mosh has been a Media and Events Volunteer Coordinator at Christ Embassy since 2017, on the volunteer production team for live events.
Mosh was a Sports Prefect at Grange School in Lagos from 2019 to 2020, responsible for about 100 students and inter house sports.

## Recently learned

Mosh recently practised API resilience: HTTP status codes, retry versus fail fast, Retry-After, backoff with a cap and jitter, logging, handling invalid JSON, and input validation.
Mosh recently practised LLM API tool use: system prompts, finish_reason, structured output, validating output, tool schemas and the two call tool flow.
Mosh recently practised SQL with SQLite: parameterized queries, idempotency, state tracking and multi step workflows.
