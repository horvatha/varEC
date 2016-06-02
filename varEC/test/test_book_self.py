"""Unittest of the Books and ExerciseBook"""
import unittest
import os
from varEC import books


text = r"""\section{Chomsky-féle nyelvtanosztályok}
\begin{feladat}{54}
Határozza meg egyesével melyik legszűkebb nyelvtan-osztályba férnek bele
az alábbi levezetési szabályok!
\ecChoose{ \[ S\rightarrow AB;\:\: S\rightarrow E;\:\: A\rightarrow Ce;\:\: C\rightarrow Cc;\:\: C\rightarrow c;\:\: F\rightarrow f;\:\: B\rightarrow b;\:\: E\rightarrow eE\:\: \]}{prod}

\vspace{3ex}
A teljes nyelvtan a \spacer[8em] nyelvtan-osztályba fér bele.

Részletezze a Chomsky-féle nyelvtan-osztályokat!

%Vezesse le lépésenként a \ecChoose{ccceb}{word} szót!
% begin table()
% prod    word
% "\[ S\rightarrow AB;\:\: S\rightarrow E;\:\: A\rightarrow Ce;\:\: C\rightarrow Cc;\:\: C\rightarrow c;\:\: FA\rightarrow fa;\:\: B\rightarrow b;\:\: bEA\rightarrow beaA\:\: \]"   \verb+ccceb+
% "\[ S\rightarrow A;\:\: S\rightarrow aBb;\:\: A\rightarrow aA;\:\: B\rightarrow ab;\:\: B\rightarrow aBb;\:\: CD\rightarrow cD;\:\: D\rightarrow dd\]"   \verb+aaabbb+
% "\[ S\rightarrow aSAC;\quad S\rightarrow abC;\quad CA\rightarrow  BA;\quad BA\rightarrow BC;\quad BC\rightarrow AC;\quad bA\rightarrow bb;\quad C\rightarrow c \]" \verb+aabbcc+
% end table
\end{feladat}

\subsection{Reguláris nyelvek, véges automaták}

\begin{feladat}{25}
Felismeri-e az alábbi determinisztikus véges automata
az üres szót és az 110011, 101 szavakat?
Határozzuk meg, melyik nyelvet ismeri fel az alábbi determinisztikus véges
automata! A választ saját szavainkkal és halmazjelöléssel is írjuk fel!
Milyen típusú nyelv ez?

\tikzset{
  >=latex,
  state/.style ={thick,circle,draw},
  finalstate/.style ={state,double}
}
\begin{tikzpicture}[scale=3]
\node[state] (S) at (0,0) {$q_0$} edge[<-,thick] (-.4,0);
\node[state] (A) at (1,0) {$q_1$};
\node[finalstate] (B) at (2,0) {$q_2$};
\path[thick,->] (S) edge[bend left=30] node[below] {1} (A)
                     edge[loop above] node[near end,right] {0} ()
                (A) edge node[below] {1} (B)
                    edge[bend left=30] node[below] {0} (S)
                (B) edge[bend right=50] node[below] {0} (S)
                     edge[loop above] node[near end,right] {1} ();
\end{tikzpicture}
\end{feladat}

\begin{feladat}{13}
Jelölje G a következő nyelvtant
$$G=(\{0;1;2\};  \{S\}; S; \{S\rightarrow0SAC; S\rightarrow01C;
CA\rightarrow BA; BA\rightarrow BC; BC\rightarrow AC; 1A\rightarrow  11;
C\rightarrow 2 \})$$
\begin{enumerate}
\item G nyelvtanban vezessük le $001222$ és $001122$ közül, amelyik levezehető!
\item Határozzuk meg ${\cal L}(G)$ nyelvet!
\item Milyen típusú a G nyelvtan?
\end{enumerate}
\begin{megoldas}
        \[{\cal L}(G)=\{0^n1^n2^n|n\ge 1\}\]
        környezetfüggő
\end{megoldas}
\end{feladat}

\begin{feladat}{14}
Adjon meg egy véges determinisztikus automatát, amely az
$\{ab^n|n\ge0\}$ nyelvet ismeri fel.
\end{feladat}

\begin{feladat}{15}
Határozzuk meg, hogy az ${\cal L}(G)$ nyelvben benne
van-e: $\varepsilon$, $abb$, $aabb$? Írjuk le szavakkal és
halmazjelölésekkel, milyen szavakat tartalmaz!
Melyik legszűkebb Chomsky-féle nyelvtan-osztályba sorolható az alábbi
nyelvtan?
\[\Sigma=\{a, b\},\quad N=\{S\}\] \[P=\{S\rightarrow ab; S\rightarrow aSb\}\]
\end{feladat}

\begin{feladat}{16}
Határozzuk meg, hogy az ${\cal L}(G)$ nyelvben benne van-e: $01$, $111$,
$1111$? Írjuk le szavakkal milyen szavakat tartalmaz!
Melyik legszűkebb Chomsky-féle nyelvtan-osztályba sorolható az alábbi
nyelvtan?
\[\Sigma=\{0, 1\},\quad N=\{S, A\},\quad P=\{S\rightarrow 1; S\rightarrow
1A; S\rightarrow 0S; A\rightarrow 1S; A\rightarrow 0A\}\]
\end{feladat}

\begin{feladat}{53}
Hozzunk létre olyan véges automatát, amely ugynazt a nyelvet ismeri fel, mint
amit az alábbi nyelvtan generál!
Határozzuk meg, hogy az ${\cal L}(G)$ nyelvben benne van-e: $01$, $111$,
$1111$?
\[\Sigma=\{0, 1\},\quad N=\{S, A\}\] \[P=\{S\rightarrow 1; S\rightarrow
1A; S\rightarrow 0S; A\rightarrow 1S; A\rightarrow 0A\}\]
\end{feladat}

\begin{feladat}{28}
Hozzunk létre olyan véges automatát, amely ugyanazt a nyelvet ismeri
fel, mint amit az alábbi nyelvtan generál!
\[G: \quad S\rightarrow 1;\: S\rightarrow 1A;\: S\rightarrow 0S;\:
A\rightarrow 1S;\: A\rightarrow 0A \]
\end{feladat}

\begin{feladat}{29}
Határozzunk meg egy olyan nyelvtant, amely ugyanazt a nyelvet generálja,
mint amit az alábbi automata felismer!

\tikzset{
  >=latex,
  state/.style ={thick,circle,draw},
  finalstate/.style ={state,double}
}
\begin{tikzpicture}[scale=3]
\node[state] (S) at (0,0) {$S$} edge[<-,thick] (-.4,0);
\node[state] (A) at (1,0) {$A$};
\node[finalstate] (B) at (2,0) {$B$};
\path[thick,->] (S) edge[bend left=30] node[below] {1} (A)
                     edge[loop above] node[near end,right] {0} ()
                (A) edge[bend left=0] node[below] {1} (B)
                    edge[bend left=30] node[below] {0} (S)
                (B) edge[bend right=50] node[below] {0} (S)
                     edge[loop above] node[near end,right] {1} ();
\end{tikzpicture}
\end{feladat}

\begin{feladat}{sixtyone}
Határozzunk meg egy olyan nyelvtant, amely ugyanazt a nyelvet generálja,
mint amit az alábbi automata felismer!

\tikzset{
  >=latex,
  state/.style ={thick,circle,draw},
  finalstate/.style ={state,double}
}
\begin{tikzpicture}[scale=3]
\node[state] (S) at (0,0) {$S$} edge[<-,thick] (-.4,0);
\node[state] (A) at (1,0) {$A$};
\node[finalstate] (B) at (2,0) {$B$};
\node[finalstate] (C) at (0,0.5) {$C$};
\path[thick,->] (S) edge[bend left=30] node[below] {b} (A)
                     edge node[left] {a} (C)
                (A) edge[bend left=0] node[below] {b} (B)
                    edge[bend left=30] node[below] {a} (S)
                (B) edge[bend right=50] node[below] {a} (S)
                     edge[loop above] node[near end,right] {b} ();
\end{tikzpicture}
\end{feladat}

%begin{definition}
\usepackage{tikz}
%end{definition}

"""
code_set = {54, 25, 13, 14, 15, 16, 53, 28, 29, 'sixtyone'}


class TestExerciseBook(unittest.TestCase):
    """"""

    def setUp(self):
        """Setup Tests"""
        self.text = text.splitlines(keepends=True)
        self.ExerciseBook = books.ExerciseBook(
            'tmp.tex',
            text=self.text,
        )

    def test_exercise_book_init(self):
        self.assertEqual(self.ExerciseBook.file_name, 'tmp.tex')
        self.assertEqual(
            set(self.ExerciseBook.code_list),
            code_set)
        self.assertEqual(len(self.ExerciseBook.exercises), len(code_set))
        first_exercise = self.ExerciseBook.exercises[0]
        self.assertIsInstance(first_exercise, books.Exercise)
        self.assertEqual(first_exercise.begin.row, 2)
        self.assertEqual(first_exercise.begin.start, 0)
        self.assertEqual(first_exercise.code, 54)
        self.assertEqual(
            str(first_exercise),
            'Exercise   54 from the row    2.')

    def test_definitions_function_get_definitions(self):
        self.assertEqual(self.ExerciseBook.definitions()[0],
                         '\\usepackage{tikz}\n')

    def test_can_list_bad_arguments(self):
        self.assertEqual(self.ExerciseBook.bad_arguments_row_and_argument(),
                         [(125, 'sixtyone')])


class TestFileFunctions(unittest.TestCase):
    """Test name_with_path function."""

    def setUp(self):
        """Setup Tests"""
        self.file_paths = ".. files/ .".split()
        self.old_directory = os.getcwd()
        test_directory = os.path.dirname(__file__)
        os.chdir(test_directory)

    def tearDown(self):
        os.chdir(self.old_directory)

    def test_can_find_files(self):
        known_values = (
            ("ec_sorter.py", ["../ec_sorter.py"]),
            ("books.py", ["../books.py", "files/books.py"]),
            ("test_possibilities.py", ["./test_possibilities.py"]),
            ("there_is_no_such_file.py", []),
            ("test", []),  # It does not find directories.
        )
        for file_name, result in known_values:
            self.assertEqual(
                books.name_with_path(file_name, self.file_paths),
                result
            )

    def test_read_file_lines(self):
        known_values = (
            ('there_is_no_such_file.py', []),
            ('files/books.py', ['"""Just for testing"""\n']),
        )
        for file, result in known_values:
            self.assertEqual(books.read_files_lines_or_empty_list(file), result)

if __name__ == "__main__":
    unittest.main()
