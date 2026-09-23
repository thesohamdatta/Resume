% Intro Options
\\ProvidesClass{resume-openfont}[2021/05/30 Abdullah's version]
\\NeedsTeXFormat{LaTeX2e}
\\DeclareOption{print}{\\def\\@cv@print{}}
\\DeclareOption*{%
    \\PassOptionsToClass{\\CurrentOption}{article}
}
\\ProcessOptions\\relax
\\LoadClass{article}

%--------------------------------------------------------------
% Package Imports
\\RequirePackage[english]{babel}
\\RequirePackage{fancyhdr}
\\RequirePackage[hmargin=1cm, vmargin=0.94cm]{geometry}
\\usepackage[hidelinks]{hyperref}
\\RequirePackage{titlesec}
\\RequirePackage{enumitem}
\\RequirePackage{tabularx}
\\RequirePackage{fontawesome}
\\RequirePackage{lato-font}
\\RequirePackage{raleway-font}
\\RequirePackage{ulem}

%--------------------------------------------------------------
% Section styling
\\titlespacing{\\section}{0pt}{3pt}{2pt}
\\titleformat{\\section}{%
\\color{headings}%
\\scshape%
\\customLatoLight%
\\fontsize{14pt}{17pt}%
\\selectfont%
\\raggedright%
\\uppercase%
} {}{0em}{}

\\titlespacing{\\subsection}{0pt}{\\parskip}{-\\parskip}
\\titleformat{\\subsection}{%
\\color{subheadings}%
\\customLatoBlack%
\\fontsize{11.5pt}{12pt}%
\\selectfont%
\\bfseries%
\\uppercase%
\\normalfont%
} {}{0em}{}

\\newcommand{\\resetHeaderAndFooter}{%
\\fancyhf{}%
\\fancyfoot{}%
\\renewcommand{\\headrulewidth}{0pt}%
\\renewcommand{\\footrulewidth}{0pt}%
}

%--------------------------------------------------------------
% Formatting commands
\\newcommand{\\NoSpace}{\\vspace*{-1pt}}
\\newcommand{\\fakeNewLine}{\\newline \\vspace{-\\baselineskip}}
\\newcommand{\\alignProfileTable}{%
    \\raggedbottom%
    \\raggedright%
    \\setlength{\\tabcolsep}{0in}%
}

\\newcommand{\\runsubsection}[1]{%
\\color{subheadings}%
\\customLatoBlack%
\\fontsize{11.5pt}{12pt}%
\\selectfont%
\\bfseries%
#1%
\\normalfont}

\\newcommand{\\descript}[1]{%
\\color{subheadings}%
\\raggedright%
\\scshape%
\\customRalewayMedium%
\\fontsize{9.5pt}{11pt}%
\\selectfont{#1}%
\\normalfont}

\\newcommand{\\location}[1]{%
\\color{headings}%
\\raggedright%
\\customRalewayMedium%
\\fontsize{9.5pt}{11pt}%
\\selectfont{#1}%
\\normalfont}

\\newcommand{\\minorSection}[1]{%
\\color{subheadings}%
\\raggedright%
\\customRalewayMedium%
\\fontsize{9.5pt}{10.5pt}%
\\selectfont{#1}%
\\normalfont}

% Project command now exposes only the linked project title, not a literal "GitHub" label.
\\newcommand{\\Project}[2]{%
\\runsubsection{\\href{#2}{\\uppercase{#1}}}%
\\hfill%
}

\\newcommand{\\underlinedLink}[2]{%
\\href{#1}{\\uline{#2}}%
}

\\newcommand{\\singleItem}[2]{\\normalsize{\\textbf{#1} #2}}
\\newcommand{\\doubleItem}[4]{\\singleItem{#1}{#2} & \\singleItem{#3}{#4}}

\\newcommand{\\sectionsep}[0]{\\vspace{4pt}}

\\newenvironment{bullets}{%
\\vspace{-1mm}%
\\begin{itemize}[leftmargin=1.15em,itemsep=1.5pt,topsep=1pt,parsep=0pt,partopsep=0pt]%
}{%
\\end{itemize}%
\\vspace{-\\topsep}%
}

\\newenvironment{skillList}{%
\\noindent%
\\begin{tabular*}{\\textwidth}{@{\\extracolsep{\\fill}}ll}%
}{%
\\end{tabular*}%
}

\\let\\oldSection\\section
\\renewcommand{\\section}[1]{\\oldSection{#1}\\raggedright}
