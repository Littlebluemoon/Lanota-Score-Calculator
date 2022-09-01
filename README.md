# Lanota Score Calculator
A simple tool to calculate the score achieved in the rhythm game, Lanota.
## How the scoring system works
As in the case of many other rhythm games such as Cytus, Deemo, etc., Lanota also features a **combo score** system, but with some twists.
### Basic values
**Base note score**: 920 000 points are split equally between all notes in the song.
A Tune note is worth only 10/23 (approx. 43.475%) of a Harmony note's base value. Combo score is not modified by this rule. 
**Combo score rules**:
1. Unlike Deemo or Cytus where combo score increases over time as your combo grows, the combo score actually *decreases* in this game.
Thus, the first note hit in every song worths the most points in any chart.
Each following notes will have its value decreased by one **combo score unit**, up to half the note count, at which point the combo score will quickly decrease to a constant value, depending on the note count:
- If the note count is odd, it is decreased quickly over the next two notes,
- otherwise, it is decreased quickly over the next note.
2. If your current combo is less than or equal to your max combo achieved in a specific song, you won't get any combo score.
E.g. You achieved a combo of 200 before Failing a note. The next note hit will not award combo score, regardless of whether it is a Harmony or Tune note.
3. The combo score's decreasing process carries over if you break a combo, but resumed it later.
E.g. You achieved a combo of 5 before Failing a note. As per the rule mentioned in **1.**, the last note hit in the previous combo has its combo score decreased by four **combo score units**. If you resume a combo later, as your combo counter hits 6, that very note will have its combo score decreased by five **combo score units**.
### Detailed score formulae:
**Base note score:** $920000 \over (note count)$ [1]
**Combo score unit:** $combo\_score\_unit = \frac{160000}{(note count)^2}$ [2]
**Difference between the maximum and minimum points awarded by a note:** $160000 \over (note count)$ [3]
**First note score:** Equals to the sum of [1] and [3], minus 0.5 **combo score units**.
$$first\_note\_score = \frac{920000}{note\_count}+\frac{160000}{note\_count}-\frac{80000}{note\_count^2}$$ [4]
**Following note scores:** Equals to [4] minus an appropriate multiple of **combo score unit**.
$$note\_score_i = first\_note\_score - i \times combo\_score\_unit\\where\text{ i} \leq \lfloor note\_count \div 2\rfloor$$ [5]
**Rapid combo score decrement:**
If note count is odd:
- the next note's score is decreased by $d_1 \times combo\_score\_unit$,
- the note following that one has its score decreased by $d_2 \times combo\_score\_unit$;
where
$$\begin{cases}d_1 + d_2 = cff\\d_1 - d_2 = 0.75\\cff = (note\_count) \div 4 + 1\end{cases}$$ [6]
otherwise:
- the next note's score is decreased by $d \times combo\_score\_unit$,
where $$d = (note\_count) \div 4 + 0.5$$