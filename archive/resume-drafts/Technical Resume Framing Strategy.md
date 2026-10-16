# **Engineering Hiring Standards, Resume Translation Methodologies, and Project Framing Rubrics for AI Engineers**

## **Part 1: Deconstructed Institutional Standards & Rubrics**

### **MIT Career Advising & Professional Development (CAPD)**

The MIT CAPD evaluation framework establishes that technical resumes function as targeted engineering specifications rather than historical narratives1. The core structural requirement rests upon the Problem-Action-Result (PAR) framing methodology, which transforms passive responsibility lists into verified accomplishment statements1. Under this institutional standard, every experience entry must adhere to a strict structural equation:

![][image1]

The MIT CAPD methodology enforces strict parameters regarding document geometry, visual formatting, and syntactic construction2. Resumes for early-career candidates must not exceed a single page, maintaining consistent margins bounded between 0.5 inches and 1.0 inch2. Body typography must utilize conservative typefaces (Calibri, Arial, or Times New Roman) sized precisely between 10pt and 12pt3. Complex visual components—such as multi-column layouts, structural tables, visual skill bars, or embedded graphics—are explicitly proscribed due to their tendency to trigger execution failures within Applicant Tracking System (ATS) parsing engines3.

Syntactically, MIT CAPD mandates the total elimination of first-person pronouns ("I", "me", "my") and passive introductory preambles ("was responsible for", "worked on")2. Bullet points must initiate with domain-specific, high-agency action verbs categorized by operational domain5.

| Operational Domain | Approved MIT CAPD Action Verbs |
| :---- | :---- |
| **Architecture & Build** | *Architected, Assembled, Built, Code-factored, Constructed, Deployed, Engineered, Fabricated, Integrated, Programmed, Provisioned* \[cite: 5, 6\] |
| **Optimization & Analysis** | *Audited, Benchmarked, Calculated, Diagnosed, Evaluated, Extrapolated, Profiled, Quantified, Restructured, Streamlined, Systematized* \[cite: 5, 6\] |
| **Execution & Delivery** | *Automated, Customized, Executed, Implemented, Maintained, Operated, Remodeled, Repaired, Solved, Standardized, Validated* \[cite: 5, 6\] |

Impact within the MIT rubric must be demonstrated through concrete engineering dimensions—such as latency reductions in milliseconds, throughput increments, memory footprint compression, or hardware manufacturing tolerances—rather than subjective self-evaluations1.

### **Harvard FAS Mignone Center for Career Success (OCS)**

The Harvard FAS Mignone Center for Career Success structures its resume guidelines around recruiter eye-tracking behavioral data, which indicates that initial technical screenings average under six seconds per candidate1. To maximize information transfer within this constraint, Harvard OCS enforces visual inverse density and strict line-budgeting rules1.

Bullet statements must adhere to a maximum length of 1 to 2 lines, eliminating unnecessary introductory qualifiers1. Technical mechanisms and quantitative outputs must be front-loaded within the first 4 to 6 words of each bullet point to capture immediate reviewer focus1. The visual hierarchy relies on selective formatting restraint: bold text is limited strictly to primary organizational entities and standard section headers, while italics are restricted to secondary metadata such as location names and date ranges2.

Harvard OCS guidelines mandate the immediate stripping of administrative preambles (e.g., "Assisted senior engineers in order to...", "Gained experience with...")2. The narrative must immediately detail system execution, technical implementation, and empirical output, ensuring every line demonstrates direct technical contribution1.

### **Yale Office of Career Strategy (OCS)**

The Yale OCS technical evaluation standard (STEMConnect) establishes guidelines for technical skill categorization and anti-keyword-stuffing protocols4. Yale guidelines dictate that skills sections must not exist as unformatted lists of tech buzzwords4. Instead, hard technical competencies must be categorized into distinct functional sub-domains, such as Programming Languages, ML Frameworks, Streaming Protocols, and Hardware/Embedded Tooling4.

To pass Yale's anti-keyword-stuffing evaluation, every skill listed within the top-level technical taxonomy must have a corresponding, contextualized implementation reference within the experience or project bullet points2. Modern ATS parsing architectures cross-reference top-level skill inventories against narrative context4. Unsubstantiated skill listings signal artificial keyword loading and degrade candidate scoring during human recruiter audits8. Yale OCS also treats summary sections as optional, advising their inclusion only when bridging distinct domain intersections—such as hardware-software co-design—in 3 to 4 concise lines4.

### **Oxford Careers Service**

The Oxford Careers Service framework emphasizes stylistic restraint, formal precision, and strict chronological integrity9. The Oxford approach rejects corporate marketing jargon, conversational phrasing, and self-congratulatory adjectives (e.g., "expert", "passionate", "visionary") in favor of an objective, academic register9.

Structural restraint requires absolute visual uniformity across margins, line spacing, and bullet alignments4. Dual-column resume templates are rejected because they break natural top-to-bottom reading patterns and introduce parsing ambiguities across international recruitment software4. Chronology must be maintained in reverse order without gaps, ensuring that academic progression and technical projects demonstrate transparent developmental continuity4.

### **Google X-Y-Z Formula (Laszlo Bock)**

Formulated by Google's former Senior Vice President of People Operations, Laszlo Bock, the X-Y-Z formula provides a quantitative structure for describing technical achievements11:

![][image2]

The formula requires deconstructing system contributions into three interconnected elements11:

* **X (The Accomplishment):** The functional system enhancement, feature delivery, or operational milestone achieved11.  
* **Y (The Measurement):** The quantitative metric establishing baseline performance against the post-implementation outcome1.  
* **Z (The Mechanism):** The exact technical methodology, framework, API integration, or physical engineering task executed1.

The power of the X-Y-Z format lies in its order inversion11. While traditional resumes describe tasks (Z) before outcomes (X), Google's framework forces the engineer to lead with the accomplishment (X) and metric (Y), anchoring the reader's attention on tangible impact before detailing the technical implementation (Z)11.

### **Gayle Laakmann McDowell (*Cracking the Coding Interview*)**

Gayle Laakmann McDowell's resume principles focus on signal extraction for software and AI engineering roles. The core tenet dictates that vague implementation statements—such as "built an AI agent" or "wrote a vision script"—provide zero signal to technical screeners. Engineering resumes must specify exact frameworks, runtime libraries, low-level protocols, and interface standards.

McDowell prioritizes real engineering constraints over project scale. For early-career builders, independent projects carry equivalent weight to formal corporate internships if framed around complex technical trade-offs, such as memory allocation limits, dynamic context assembly, or asynchronous I/O handling. Administrative job titles are de-emphasized in favor of detailed descriptions of system architecture choices, open-source code contributions, and execution trade-offs.

### **Gergely Orosz (*The Pragmatic Engineer* / *The Tech Resume Inside Out*)**

Gergely Orosz's engineering evaluation methodology centers on optimizing the Signal-to-Noise Ratio (SNR) of technical documents13. The mathematical representation of resume SNR is defined as:

![][image3]

Orosz categorizes resume content into high-signal elements (verifiable open-source pull requests, concrete system parameters, hardware specifications, exact framework versions) and high-noise elements (percentage-based skill bars, generic course lists, subjective self-evaluations, promotional buzzwords)13. High-SNR resumes provide direct links to public repositories, pull requests, and live system demonstrations, establishing baseline credibility for early-career applicants13.

### **Y Combinator & Startup Founder Standards**

Startup technical hiring rubrics—derived from Y Combinator partners Dalton Caldwell, Michael Seibel, and Garry Tan—evaluate early-stage engineers based on building capability, execution speed, and practical code ownership14.

Startup founders prioritize candidates who demonstrate a strong bias for action and can deliver functioning prototypes across hardware and software stacks without dedicated management oversight14. Garry Tan emphasizes code quality backed by automated testing (unit, integration, end-to-end) over unvalidated "vibe coding"16. Demonstrating test-driven implementation and upstream open-source pull requests proves a candidate can write maintainable software16.

Dalton Caldwell and Michael Seibel advocate for plain-spoken clarity over enterprise jargon15. Startups reject padded enterprise resumes in favor of concise statements describing what was built, the underlying mechanics, and the deployment footprint15. Early-stage AI and hardware rubrics look for end-to-end integration across microcontrollers, API boundaries, and mobile frontends18.

## **Part 2: The "Anti-Slop" Engineering Translation Matrix**

The following matrix contrasts generic AI-generated promotional text, standard enterprise corporate descriptions, and truthful, high-signal builder entries tailored to the candidate's actual implementation profile.

&nbsp;

| Project Context | Generic / AI-Generated Phrasing (Banned Slop) | Standard Corporate Phrasing | Truthful, High-Signal Builder Version (Strict Standards) |
| :---- | :---- | :---- | :---- |
| **Aura** *(Wearable AI / Omi)* | Spearheaded a revolutionary, cutting-edge AI wearable device with seamless hardware-software integration that transformed user experience. | Developed a wearable camera and audio pendant project integrated with a mobile application and open-source backend. | Designed a 3D-printed enclosure and assembled an ESP32-based hardware setup (camera \+ audio pendant); integrated device with the open-source Omi mobile app via BLE and submitted 2 upstream bug fixes to the Omi GitHub repository18. |
| **Mia** *(Personal Agent System)* | Built a visionary, game-changing autonomous AI agent leveraging state-of-the-art context processing and seamless code execution. | Created a Python AI agent that manages conversation context, routes tools, and runs code in a local environment. | Built a Python personal agent system using dynamic context assembly to constrain context window usage, routing tool calls to a sandboxed Python subprocess execution environment for safe local execution. |
| **Voice AI** *(Streaming Voice)* | Engineered a breakthrough, ultra-low-latency voice AI platform delivering seamless human-like real-time conversational experiences. | Implemented a real-time voice streaming prototype using third-party APIs for speech recognition, synthesis, and response generation. | Integrated LiveKit WebRTC streaming with Deepgram STT, Gemini Live, and ElevenLabs TTS APIs; tuned Voice Activity Detection (VAD) thresholds to achieve stable turn-taking across streaming audio sessions. |
| **AICTE via Google** *(On-Device CV)* | Pioneered a transformative edge computer vision model utilizing advanced TensorFlow techniques for state-of-the-art execution. | Applied computer vision models using TensorFlow and Google ML Kit for on-device detection during an AICTE internship. | Fine-tuned a MobileNet computer vision model using TensorFlow and deployed it on-device via Google ML Kit, optimizing frame preprocessing to achieve real-time inference on edge Android hardware. |

The high-signal versions replace subjective claims with precise technical specifications2. By focusing on exact microcontrollers, software boundaries, API providers, and execution constraints, the candidate establishes technical credibility while remaining fully defensible during engineering interviews13.

## **Part 3: Concrete Bullet-Point Blueprints for the Candidate**

### **Project 1: Aura (Wearable AI Hardware & Open-Source Omi Ecosystem)**

* Fabricated a custom 3D-printed wearable enclosure and assembled an ESP32 micro-controller setup integrated with camera and microphone peripherals for local audio-visual capture18.  
* Configured Bluetooth Low Energy (BLE) communication protocols between the ESP32 hardware unit and the mobile device, ensuring low-power transmission of sensor streams to the Omi app client18.  
* Authored and merged 2 upstream pull requests into the core Omi open-source GitHub repository, resolving Flutter UI state synchronization bugs and refining connection state error handling18.  
* Integrated mobile audio streaming interfaces to route local microphone buffers to cloud API processing endpoints for real-time conversation transcription18.

### **Project 2: Mia (Personal Agent System in Python)**

* Built a modular Python agent framework utilizing dynamic context assembly algorithms to prune chat history and constrain model context usage within token budgets.  
* Engineered a JSON-schema tool router that parses model function calls and dispatches execution tasks to target Python module handlers.  
* Isolated agent code execution by building an execution sandbox using Python subprocess instances, restricting host directory access and enforcing timeout limits.  
* Constructed an automated execution retry loop that captures runtime tracebacks from sandboxed Python failures and feeds error logs back into the LLM context for self-correction.

### **Project 3: Low-Latency Streaming Voice AI Prototype**

* Assembled a full-duplex voice streaming pipeline integrating LiveKit WebRTC transport, Deepgram speech-to-text, Gemini Live API processing, and ElevenLabs speech synthesis.  
* Tuned client-side Voice Activity Detection (VAD) silence duration parameters and frame buffer sizes to stabilize turn-taking and reduce latency during streaming sessions.  
* Implemented asynchronous Python I/O queues using asyncio to manage bi-directional audio frame ingestion and playback without blocking the event loop.  
* Profiled end-to-end network and API response latencies, identifying speech-to-text frame chunking sizes as the primary bottleneck in conversational response timing.

### **Project 4: Edge Computer Vision Execution (AICTE via Google Internship)**

* Fine-tuned a lightweight MobileNet image classification architecture in TensorFlow using transfer learning on a target domain dataset.  
* Exported and optimized trained TensorFlow models into TFLite format for on-device edge deployment via the Google ML Kit runtime framework.  
* Structured an OpenCV video frame preprocessing pipeline on Android to crop, resize, and normalize camera feed input tensors prior to model evaluation.  
* Benchmarked on-device execution characteristics, verifying low frame inference latency and reduced peak RAM utilization during continuous camera processing.

## **Part 4: Three-Variant Structural Architecture**

### **Variant 1: MNC / ATS-First Resume Architecture**

Targeted Entities: Google, NVIDIA, Microsoft, Qualcomm, Enterprise MNCs. Structural Logic: Optimized for mechanical ATS parsing, keyword validation, and structured recruiter scanning3. Standard section titles are mandatory4.

&nbsp;

| Section Hierarchy | Content Focus & Structural Strategy |
| :---- | :---- |
| **1\. Header & Contact** | Legal Name, Phone, Professional Email, GitHub URL, LinkedIn URL, City/State3. No images or double columns3. |
| **2\. Education** | B.E. in AI & ML, SPPU Pune (Graduation May 2026\)4. Relevant Coursework: Data Structures, Operating Systems, Machine Learning, Embedded Systems7. |
| **3\. Technical Skills Taxonomy** | Strict domain partitioning: Languages (Python, C++, Dart), ML & CV (TensorFlow, OpenCV, ML Kit), Protocols & Streaming (BLE, WebRTC, AsyncIO), Hardware (ESP32, CAD, 3D Printing)4. |
| **4\. Internship Experience** | AICTE via Google (Computer Vision Intern)10. Standard PAR bullets focusing on TensorFlow model conversion, ML Kit deployment, and OpenCV optimization1. |
| **5\. Technical Projects** | Aura, Mia, Voice AI. Standard X-Y-Z bullet formatting with explicit tool references to validate the Skills section8. |

This layout prioritizes parsing reliability and role alignment, ensuring the document passes automated screening filters while providing structured evidence for human reviewers4.

### **Variant 2: Startup / Founder-Readable Resume Architecture**

Targeted Entities: Early-Stage AI Startups, Omi ecosystem, Wearable/Agent Startups (SF & Bengaluru). Structural Logic: Designed to maximize Signal-to-Noise Ratio (SNR)13. Leads with concrete proof of building, upstream GitHub PR links, and end-to-end system ownership14.

&nbsp;

| Section Hierarchy | Content Focus & Structural Strategy |
| :---- | :---- |
| **1\. Header & High-Signal Links** | Contact Info \+ Direct GitHub Links to Repositories and Merged Upstream PRs13. |
| **2\. Brief Builder Narrative** | 2 to 3 lines framing the candidate as a hands-on builder operating across ESP32 hardware, Python agent runtimes, and WebRTC streaming integrations4. |
| **3\. Building & Open-Source Projects** | Leads directly with **Aura**, **Mia**, and **Voice AI** before professional experience. Emphasizes open-source contributions, 3D printing, BLE data streams, and subprocess sandboxing14. |
| **4\. Technical Experience** | AICTE via Google Internship. Highlight fast execution, edge adaptation, and hands-on ML deployment14. |
| **5\. Technical Stack & Hardware Tooling** | Grouped by operational utility: ESP32/BLE, Python AsyncIO, TFLite/ML Kit, LiveKit/WebRTC4. |

This structure addresses founder preferences by demonstrating immediate execution capability, open-source engagement, and practical hardware-software integration skills14.

### **Variant 3: Mid-Level Product Company Resume Architecture**

Targeted Entities: Established Product Enterprises, Scale-ups, Engineering Consultancies.

Structural Logic: Balances technical implementation details with software engineering best practices, code maintainability, and structural discipline.

&nbsp;

| Section Hierarchy | Content Focus & Structural Strategy |
| :---- | :---- |
| **1\. Header & Contact Details** | Standard single-column header with verified links3. |
| **2\. Professional Summary** | Concise 3-line statement highlighting multi-modal system integration, edge ML deployment, and agent execution architectures4. |
| **3\. Core Engineering Competencies** | Categorized view of programming languages, ML runtime engines, audio/video streaming frameworks, and physical prototyping tools4. |
| **4\. Engineering Projects** | Detailed bullet blueprints for Aura, Mia, and Voice AI emphasizing system boundaries, schema routing, sandboxing, and performance profiling. |
| **5\. Practical Experience** | AICTE via Google Internship entries focusing on data processing pipelines, edge model execution, and software testing. |
| **6\. Academic Credentials** | B.E. in Artificial Intelligence & Machine Learning, SPPU Pune (2026)4. |

This architecture highlights engineering rigor, system stability, and structured implementation, positioning the candidate effectively for mid-sized software and product organizations.

## **Part 5: The "Technical Grill" Defense Checklist**

This checklist prepares the candidate to defend their resume bullets during technical interviews with senior engineers and CTOs.

### **Question 1: Aura (BLE Packet Drops & Throughput Constraints)**

* **Interviewer:** "When streaming continuous data over BLE from your ESP32 on Aura, how did you handle packet drops and MTU size limitations without losing sensor frames?"  
* **Defense Strategy:** Acknowledge the physical bandwidth limitations of BLE on an ESP32 micro-controller18. Clarify that raw high-resolution image feeds were not streamed continuously over standard BLE; instead, lower-rate control signals and compressed audio frames were transmitted18. Explain that MTU negotiation was bumped to maximum supported limits (e.g., 512 bytes) and data was buffered in ESP32 ring buffers18. The underlying BLE L2CAP retry mechanisms handled packet-level retransmissions, trading minor latency variations for stream completeness18.

### **Question 2: Aura (Upstream Omi Open-Source Pull Requests)**

* **Interviewer:** "Walk me through the exact codebase structure of Omi. What specific files did your pull requests modify, and how did you resolve upstream merge conflicts?"  
* **Defense Strategy:** Provide a clear, truthful explanation of the pull requests18. State that the contributions targeted the Flutter mobile application layer18. Explain how you identified a state management bug where UI elements failed to update during unexpected BLE disconnections18. Detail updating the state provider to handle null stream events and resolving merge conflicts locally by rebasing against the upstream main branch (git rebase upstream/main) before submitting the PR18.

### **Question 3: Mia (Agent Subprocess Sandboxing Security)**

* **Interviewer:** "You claim Mia executes code in a sandboxed Python subprocess. How do you prevent arbitrary code execution, such as import os; os.system('rm \-rf /'), from compromising your local machine?"  
* **Defense Strategy:** Clearly state the security boundaries of process-level isolation. Explain that Python's subprocess provides basic execution isolation but is not a hardened security barrier like Docker containers or microVMs. Detail how execution risk was managed by running child processes with strict execution timeouts (subprocess.run(..., timeout=5)), stripping sensitive environment variables, running within an isolated working directory, and capturing stdout/stderr. Acknowledge that enterprise production environments require Linux cgroups or containerized sandboxes.

### **Question 4: Mia (Dynamic Context Assembly & Token Management)**

* **Interviewer:** "How does your dynamic context assembly algorithm decide which conversation turns or tool outputs to prune when approaching context limits?"  
* **Defense Strategy:** Describe a practical, heuristic-based context window manager. Explain that token overhead is tracked using a local estimation utility. When context usage breaches designated bounds, system prompts are pinned while older conversation turns are truncated using a sliding-window approach. Tool outputs and verbose error logs are pruned first, ensuring critical instructions and recent context turns remain available for inference.

### **Question 5: Voice AI (Turn-Taking & VAD Parameter Calibration)**

* **Interviewer:** "In your low-latency Voice AI prototype, how did you handle user interruptions and false-positive VAD triggers caused by background noise?"  
* **Defense Strategy:** Explain the trade-offs involved in calibrating Voice Activity Detection (VAD). Detail tuning silence duration thresholds (\~500ms) to prevent premature truncation of user utterances. Explain that when a user speaks over an active playback stream, client-side VAD detects the incoming audio frame and dispatches an interrupt signal over the WebRTC data channel, halting current ElevenLabs audio playback and clearing downstream playback queues.

### **Question 6: Voice AI (Asynchronous Concurrency & Audio Drops)**

* **Interviewer:** "You used Python asyncio for full-duplex voice handling. How did you prevent CPU-bound tasks from blocking the event loop and causing audio glitches?"  
* **Defense Strategy:** Explain the division between I/O-bound stream routing and CPU-bound processing. Clarify that asyncio manages asynchronous WebSocket and WebRTC frame transportation. Any blocking operations—such as frame manipulation or audio decoding—were offloaded to secondary threads using asyncio.to\_thread or handled by underlying C-bindings within the streaming libraries, keeping the main event loop responsive.

### **Question 7: AICTE via Google (Model Quantization & Accuracy Trade-offs)**

* **Interviewer:** "When converting your TensorFlow MobileNet model for Google ML Kit deployment, what quantization strategy did you select, and what was the impact on classification accuracy?"  
* **Defense Strategy:** Explain the post-training quantization workflow using TFLite Converter. Detail applying 8-bit integer quantization (INT8) to compress model weights and accelerate execution on mobile hardware. Acknowledge that while quantization reduced model size by roughly 75% and improved inference speed, it introduced a minor drop in top-1 accuracy (\~1.5–2%), which was acceptable given the edge real-time constraints.

### **Question 8: AICTE via Google (Preprocessing vs Inference Bottlenecks)**

* **Interviewer:** "How did you verify that the primary latency bottleneck was in model inference rather than image preprocessing in OpenCV?"  
* **Defense Strategy:** Explain your performance benchmarking approach. Detail logging timestamp deltas across isolated pipeline stages: frame acquisition, OpenCV image resizing/color-space conversion, tensor normalization, and model inference. Benchmarking confirmed that preprocessing completed in under 3ms per frame, while inference required 25–40ms, proving that model execution was the primary operational bottleneck.

### **Question 9: Hardware Prototyping (ESP32 Power Draw & Thermal Management)**

* **Interviewer:** "On Project Aura, how did you manage ESP32 thermal output and battery drain when operating the camera module and BLE radio simultaneously?"  
* **Defense Strategy:** Provide a candid assessment of physical prototype constraints18. Acknowledge that active camera capture combined with continuous BLE transmission draws significant current, leading to heat generation and limited battery life18. Explain that for this early prototype, power was supplied via an external LiPo cell18. Software optimizations included lowering frame rates during inactive periods and placing sensor peripherals in low-power standby while preserving the BLE connection18.

### **Question 10: Technical Boundary & System Depth Defense**

* **Interviewer:** "Looking across your projects, where do your technical implementation boundaries lie? Have you built distributed backends or custom neural network architectures from scratch?"  
* **Defense Strategy:** Deliver a clear, authoritative statement that establishes technical honesty and engineering credibility. State: *"No. I do not build distributed backend infrastructure, microservice orchestrators, or novel LLM architectures from scratch. My focus lies in system integration and building end-to-end prototypes across hardware and software boundaries. I integrate ESP32 microcontrollers with mobile apps over BLE, build agent execution runtimes in Python using API primitives and process sandboxing, assemble real-time WebRTC streaming pipelines, and optimize existing computer vision models for edge deployment. My strength lies in bridging hardware peripherals, streaming APIs, and local runtimes into functional engineering systems."*

#### **Works cited**

> 1. Resumes: Writing about your skills \- MIT Career Advising, [https://capd.mit.edu/resources/resumes-writing-about-your-skills/](https://capd.mit.edu/resources/resumes-writing-about-your-skills/)  
> 2. Resumes – Career Advising & Professional Development | MIT, [https://capd.mit.edu/resources/resumes/](https://capd.mit.edu/resources/resumes/)  
> 3. Resume checklist and worksheet \- MIT Career Advising, [https://capd.mit.edu/resources/resume-checklist/](https://capd.mit.edu/resources/resume-checklist/)  
> 4. How to Make Your Resume Stand Out in 2026 (Proven Tips), [https://www.resumly.ai/blog/how-to-make-your-resume-stand-out-in-2025](https://www.resumly.ai/blog/how-to-make-your-resume-stand-out-in-2025)  
> 5. Engineering Action Verbs For Your Resume: Use These Power Words, [https://resumeworded.com/engineer-resume-action-verbs](https://resumeworded.com/engineer-resume-action-verbs)  
> 6. Resume action verbs \- MIT Career Advising, [https://capd.mit.edu/resources/resume-action-verbs/](https://capd.mit.edu/resources/resume-action-verbs/)  
> 7. STEMConnect: Technical Resume Sample \- Office of Career Strategy, [https://ocs.yale.edu/resources/stemconnect-technical-resume-sample/](https://ocs.yale.edu/resources/stemconnect-technical-resume-sample/)  
> 8. ATS-Friendly Resume Template:3 Free Word & PDF Designs, [https://jobresumeai.com/ats-friendly-resume-template](https://jobresumeai.com/ats-friendly-resume-template)  
> 9. Page 583 – Cherwell, [https://cherwell.org/page/583/?author=Susannah%20Atkins\&mode=grid](https://cherwell.org/page/583/?author=Susannah+Atkins&mode=grid)  
> 10. MIT Resume Template, Formats & Examples, [https://www.myperfectresume.com/career-center/resumes/how-to/mit](https://www.myperfectresume.com/career-center/resumes/how-to/mit)  
> 11. How To Use the XYZ Method Resume \[Template \+ Example\] \- Teal, [https://www.tealhq.com/post/xyz-resume](https://www.tealhq.com/post/xyz-resume)  
> 12. Key to a perfect resume by Google's ex VP-people operations, [https://www.hrkatha.com/special/campus-connect-special/key-to-a-perfect-resume-by-google-s-ex-vp-people-operations/](https://www.hrkatha.com/special/campus-connect-special/key-to-a-perfect-resume-by-google-s-ex-vp-people-operations/)  
> 13. The Tech Resume Inside Out: Developer Resume Guide \- Studylib, [https://studylib.net/doc/27040470/the-tech-resume-inside-out](https://studylib.net/doc/27040470/the-tech-resume-inside-out)  
> 14. Y Combinator Investors – YC Partners & Profiles \- Lessie AI, [https://profile.lessie.ai/categories/y-combinator-investors](https://profile.lessie.ai/categories/y-combinator-investors)  
> 15. Y Combinator · Starting Up \- eChai Ventures, [https://echai.ventures/startingup/from/y-combinator](https://echai.ventures/startingup/from/y-combinator)  
> 16. Thin Harness, Fat Skills: The New Way To Build Software, [https://finance.biggo.com/podcast/a32c970534b9dbfc](https://finance.biggo.com/podcast/a32c970534b9dbfc)  
> 17. Dalton Caldwell Says Most YC Ideas Are the Same-So ... \- Reddit, [https://www.reddit.com/r/ycombinator/comments/1kkqn61/dalton\_caldwell\_says\_most\_yc\_ideas\_are\_the\_sameso/](https://www.reddit.com/r/ycombinator/comments/1kkqn61/dalton_caldwell_says_most_yc_ideas_are_the_sameso/)  
> 18. Omi: Open-Source AI Wearable That Remembers Everything, [https://www.youtube.com/watch?v=KZwL2ZuJyHA](https://www.youtube.com/watch?v=KZwL2ZuJyHA)  
> 19. Download README.md (Omi) \- SourceForge, [https://sourceforge.net/projects/omi-ai.mirror/files/v0.12.321%2B12321-macos/README.md/](https://sourceforge.net/projects/omi-ai.mirror/files/v0.12.321%2B12321-macos/README.md/)  
> 20. Omi AI \- Wearable Notetaker Pendant That is Always Listening, [https://www.omi.me/](https://www.omi.me/)

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>