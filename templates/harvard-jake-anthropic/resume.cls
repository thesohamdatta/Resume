% Harvard/Jake-style compact resume class, adapted for A4 and Anthropic-like typography.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume-harvard-anthropic}[2026/09/23]
\LoadClass[11pt,a4paper]{article}

\RequirePackage[margin=0.58in]{geometry}
\RequirePackage{fontspec}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage{fancyhdr}
\RequirePackage{tabularx}
\RequirePackage{microtype}
\RequirePackage{xcolor}
\RequirePackage{setspace}

% Anthropic-like type treatment. ABC Diatype is used when locally available.
\IfFontExistsTF{ABC Diatype}{
  \setmainfont{ABC Diatype}
}{
  \IfFontExistsTF{Inter}{
    \setmainfont{Inter}
  }{
    \setmainfont{Arial}
  }
}

\hypersetup{colorlinks=true,urlcolor=black}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}\setlength{\tabcolsep}{0pt}\setlength{\parskip}{0pt}
\raggedright\raggedbottom\urlstyle{same}\setstretch{0.98}
\tolerance=1800\emergencystretch=1.5em\hyphenpenalty=8000

\titleformat{\section}
  {\large\bfseries\scshape}{}{0pt}{}
  [\vspace{-4pt}\titlerule\vspace{-5pt}]
\titlespacing*{\section}{0pt}{7pt}{4pt}

\newcommand{\resumeItem}[1]{\item\small{#1\vspace{-1.5pt}}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.18in,label=\textbullet,itemsep=1.2pt,topsep=1pt,parsep=0pt,partopsep=0pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-3pt}}
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0pt,label={},itemsep=4pt,topsep=0pt,parsep=0pt,partopsep=0pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeSubheading}[4]{%
  \item
  \begin{tabularx}{\textwidth}{@{}X r@{}}
    \textbf{#1} & \textbf{#2}\\
    \textit{\small #3} & \textit{\small #4}\\
  \end{tabularx}\vspace{-3pt}}
\newcommand{\resumeProjectHeading}[2]{%
  \item
  \begin{tabularx}{\textwidth}{@{}X r@{}}
    \textbf{#1} & \textit{\small #2}\\
  \end{tabularx}\vspace{-3pt}}
\newcommand{\resumeSkill}[2]{\textbf{#1:} #2\\[-1pt]}
\endinput
