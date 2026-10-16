\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume}[2026/10/16 shared interface preserving the approved Lato template]
\LoadClass[10pt]{article}

\RequirePackage[a4paper,top=0.52in,bottom=0.54in,left=0.60in,right=0.60in]{geometry}
\RequirePackage{fontspec}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage{hyperref}
\RequirePackage{xcolor}
\RequirePackage{tabularx}
\RequirePackage{microtype}

\setmainfont{Lato}
\hypersetup{colorlinks=true,urlcolor=black,linkcolor=black}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\raggedbottom
\raggedright
\tolerance=1800
\emergencystretch=1.5em
\hyphenpenalty=10000
\urlstyle{same}

\definecolor{ResumeGray}{HTML}{666666}
\definecolor{ResumeBlack}{HTML}{111111}

\titleformat{\section}
  {\color{ResumeBlack}\large\bfseries\scshape}
  {}{0pt}{}
\titlespacing*{\section}{0pt}{6.5pt}{0pt}

\newenvironment{resumeitemize}
  {\begin{itemize}[leftmargin=15pt,itemsep=1.1pt,topsep=1pt,parsep=0pt,partopsep=0pt]}
  {\end{itemize}}

% The four-argument interface keeps contact details separate in the source while
% preserving the approved one-row contact treatment.
\newcommand{\resumeHeader}[4]{%
\begin{center}
{\fontsize{22.5}{24.5}\selectfont\bfseries #1}\\[1pt]
{\small\color{ResumeGray}#2}\\[2pt]
{\footnotesize #3\if\relax\detokenize{#4}\relax\else\ | #4\fi}
\end{center}
\vspace{-2pt}}

\newcommand{\resumeRole}[4]{%
\begin{tabularx}{\textwidth}{@{}X r@{}}
\textbf{#1} \textnormal{\,|\,#2} & \textbf{#3}\\[-1pt]
\multicolumn{2}{@{}l@{}}{\footnotesize\color{ResumeGray} #4}
\end{tabularx}
\par\vspace{1pt}}

\newcommand{\resumeProject}[3]{%
\begin{tabularx}{\textwidth}{@{}X r@{}}
\textbf{#1} & {\footnotesize #2}\\[-1pt]
\multicolumn{2}{@{}l@{}}{\footnotesize\color{ResumeGray} #3}
\end{tabularx}
\par\vspace{0.5pt}}

\newcommand{\resumeSkills}[2]{\textbf{#1} #2\par\vspace{1pt}}
\newcommand{\tightpar}[1]{{\small #1}}

\newcommand{\resumeEducation}[3]{%
\begin{tabularx}{\textwidth}{@{}X r@{}}
\textbf{#1} & \textbf{#2}\\[-1pt]
\multicolumn{2}{@{}l@{}}{\small #3}
\end{tabularx}}
\endinput
