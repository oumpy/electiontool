# ElectionTool

## What's this ?
Python会の正式名称最終投票のために作成した、簡易選挙ツールです。

## Scripts
### election.py
単記移譲式反復投票を行います。
毎回の投票では、自分以下の全てを足しても上の候補に及ばない候補と、それ以下の全候補が落選します。

フルスクラッチ実装のため、特にパッケージは必要ありません。

### election_schulze.py
Schulze法による当選者決定を行います。

こちらはパッケージ `python3-vote-core` のインストールが必要です。
pipでインストールすることができます。

## Usage
使い方は `election.py`, `election_schulze.py` どちらも同じです。

1人の投票は、候補の記号を選好順に1以上の任意個数並べたものとします。  
(Schulze法で許容されている同順位は、ここでは採用していません。)  
それらを並べて1人1行のテキストファイルとします。

それを標準入力にリダイレクトしてスクリプトを実行します。
```
$ python election.py < votes.txt
```

入力ファイルの例 (`votes.txt`)

```
ABC
EDBACFG
CABD
BFCGA
FBDACG
DBAC
CBDAFEG
BC
BCDAF
DBACFEG
DBACF
DFBEACG
DABCFEG
DBFACE
BADFC
DACBF
BFEDGAC
DBCA
DBA
```

実行結果 (`election.py` の場合)
```
The 1-th vote: [('D', 9), ('B', 5), ('C', 2), ('A', 1), ('E', 1), ('F', 1)]
  Candidates ['D', 'B', 'C'] survived.
The 2-th vote: [('D', 10), ('B', 7), ('C', 2)]
---
The candidate 'D' is the Final Winner !!!
```

実行結果 (`election_schulze.py` の場合)
```
candidates: {'G', 'D', 'F', 'C', 'A', 'E', 'B'}
winner: D
pairs: {('G', 'D'): 1, ('G', 'F'): 0, ('G', 'C'): 1, ('G', 'A'): 2, ('G', 'E'): 2, ('G', 'B'): 0, ('D', 'G'): 16, ('D', 'F'): 14, ('D', 'C'): 13, ('D', 'A'): 14, ('D', 'E'): 14, ('D', 'B'): 10, ('F', 'G'): 13, ('F', 'D'): 3, ('F', 'C'): 6, ('F', 'A'): 5, ('F', 'E'): 12, ('F', 'B'): 2, ('C', 'G'): 17, ('C', 'D'): 6, ('C', 'F'): 12, ('C', 'A'): 6, ('C', 'E'): 15, ('C', 'B'): 3, ('A', 'G'): 16, ('A', 'D'): 4, ('A', 'F'): 13, ('A', 'C'): 13, ('A', 'E'): 15, ('A', 'B'): 4, ('E', 'G'): 7, ('E', 'D'): 2, ('E', 'F'): 1, ('E', 'C'): 3, ('E', 'A'): 3, ('E', 'B'): 1, ('B', 'G'): 19, ('B', 'D'): 9, ('B', 'F'): 17, ('B', 'C'): 16, ('B', 'A'): 15, ('B', 'E'): 18}
strong_pairs: {('D', 'G'): 16, ('D', 'F'): 14, ('D', 'C'): 13, ('D', 'A'): 14, ('D', 'E'): 14, ('D', 'B'): 10, ('F', 'G'): 13, ('F', 'E'): 12, ('C', 'G'): 17, ('C', 'F'): 12, ('C', 'E'): 15, ('A', 'G'): 16, ('A', 'F'): 13, ('A', 'C'): 13, ('A', 'E'): 15, ('E', 'G'): 7, ('B', 'G'): 19, ('B', 'F'): 17, ('B', 'C'): 16, ('B', 'A'): 15, ('B', 'E'): 18}
---
The candidate 'D' is the Final Winner !!!
```