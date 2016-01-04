# geneses.py - Generate geneses.tex
# This software is GPLv3+, its output in this repository is licensed BY-SA 4.0.
# Copyright (C) 2016  Rhea Myers rhea@myers.studio
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import csv, mnemonic

from binascii import unhexlify

TOC_STRIDE = 20
TOTAL_COINS = 100

m = mnemonic.Mnemonic('english')

################################################################################
# Assemble the text for the table of contents and the poem
################################################################################

poem = "\\begin{verse}\n\\poemtitle{Geneses}\n"

toc = "\\poemtitle{Coins by Market Cap as of 2016-01-02}\n\\begin{center}\n\\begin{tabular}{ r | l }\n"

count = 0

with open('genesis-blocks.csv', 'r') as csvfile:
     csvreader = csv.reader(csvfile)
     for row in csvreader:
          if row[0].startswith("#"):
               continue
          index = int(row[0])
          coin = row[1]
          genesis = row[2]
          if (count % TOC_STRIDE) == (TOC_STRIDE - 1) \
             and (index != TOTAL_COINS):
               toc += "\\end{tabular}\n\\end{center}\n\\newpage\n\\begin{center}\n\\begin{tabular}{ r | l }\n"
          toc += "    %s & %s \\\\\n" % (index, coin)
          poem += ("\\flagverse{%s.} " % index) + m.to_mnemonic(unhexlify(genesis)) + "\n\n"
          count = count + 1

toc += "\\end{tabular}\n\n\\end{center}\n\\newpage\n\n"
poem += "\\end{verse}\n"

################################################################################
# Print everything out
################################################################################

print r'''\documentclass{book}

\usepackage{geometry}
\geometry{a6paper}

\usepackage[utf8]{inputenc}
\usepackage{libertine}
\usepackage{verse}
\usepackage{graphicx}
\usepackage[hidelinks]{hyperref}

% Don't hyphenate at line ends
\usepackage[none]{hyphenat}

% Don't break paragraphs across pages
\widowpenalties 1 10000
\raggedbottom

% Don't indent run-on lines in stanzas

\newlength{\savevindent}
\setlength{\savevindent}{\vindent}
\setlength{\vindent}{0em}

\begin{document}

\title{Geneses}
\author{Rhea Myers}
\date{}
\maketitle

\newpage
\vspace*{\fill}
\centerline{\href{https://rhea.art/}{rhea.art}}
\medskip
\centerline{\href{https://gitlab.com/rheaplex/geneses/}{gitlab.com/rheaplex/geneses}}
\medskip
\centerline{Copyright \copyright 2016}
\begin{center}
\leavevmode
\includegraphics[scale=0.6]{by-sa}
\end{center}
\label{fig:cc}
\centering{``Geneses'' by Rhea Myers is licensed under a\\\href{http://creativecommons.org/licenses/by-sa/4.0/}{Creative Commons Attribution-ShareAlike 4.0 International License.}}

\newpage
\vspace*{\fill}
\begin{flushleft}
With thanks to Seryna.
\end{flushleft}
\vspace*{\fill}

\newpage
% Blank page
\vspace*{\fill}

\newpage
\vspace*{\fill}
\begin{flushleft}
A poem consisting of\\the genesis block hashes from\\the hundred cryptocurrencies with\\the highest market capitalization\\on January the Second, 2016\\encoded as \href{https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki}{BIP039} mnemonics.
\end{flushleft}
\vspace*{\fill}

\newpage
% Blank page
\vspace*{\fill}

\newpage
''' + poem + toc + r'''

\setlength{\vindent}{\savevindent}

\end{document}
'''
