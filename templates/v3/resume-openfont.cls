\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume-openfont}[2026/09/23 canonical resume class]
\LoadClass[10pt]{article}

\RequirePackage[a4paper,top=0.55in,bottom=0.55in,left=0.62in,right=0.62in]{geometry}
\RequirePackage{fontspec}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage{hyperref}
\RequirePackage{tabularx}
\RequirePackage{microtype}

\setmainfont{Lato}
\hypersetup{colorlinks=true,urlcolor=black,linkcolor=black}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\raggedbottom
\tolerance=2000
\emergencystretch=2em
\hyphenpenalty=10000
\urlstyle{same}

\newcommand{\resumeRule}{\vspace{-5pt}\hrule\vspace{4pt}}
\titleformat{\section}{\large\bfseries\scshape}{}{0pt}{}[\resumeRule]
\titlespacing*{\section}{0pt}{7pt}{0pt}

\newenvironment{resumeitemize}
{\begin{itemize}[leftmargin=14pt,itemsep=1.4pt,topsep=1.5pt,parsep=0pt,partopsep=0pt]}
{\end{itemize}}

\newcommand{\resumeHeader}[3]{%
\begin{center}
{\fontsize{23}{25}\selectfont\bfseries #1}\\[2pt]
{\small #2}\\[2pt]
{\footnotesize #3}
\end{center}
\vspace{-3pt}}

\newcommand{\resumeRole}[4]{%
\begin{tabularx}{\textwidth}{@{}X r@{}}
\textbf{#1} \textnormal{\,|\,#2} & \textbf{#3}\\[-1pt]
\multicolumn{2}{@{}l@{}}{\footnotesize #4}
\end{tabularx}
\vspace{1pt}}

\newcommand{\resumeProject}[3]{%
\begin{tabularx}{\textwidth}{@{}X r@{}}
\textbf{#1} & {\footnotesize #2}\\[-1pt]
\multicolumn{2}{@{}l@{}}{\footnotesize #3}
\end{tabularx}
\vspace{1pt}}

\newcommand{\resumeEducation}[3]{%
\begin{tabularx}{\textwidth}{@{}X r@{}}
\textbf{#1} & \textbf{#2}\\[-1pt]
\multicolumn{2}{@{}l@{}}{\small #3}
\end{tabularx}
}

\newcommand{\resumeSkills}[2]{\textbf{#1} #2\par\vspace{1.2pt}}
\newcommand{\tightpar}[1]{{\small #1}}
\endinput
