# One Star for Monday

[![make.fun](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/funtoons/one-star-for-monday/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/funtoons/one-star-for-monday/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)

A one-star review of Monday, written as if Monday were a restaurant.
An entry for the [One Star for Monday](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
bounty on make.fun.

## The review

> One star. The waiter took my weekend away, served cold coffee and a
> lukewarm to-do list, then charged me for Monday. Would not return.

One line of plain text: 24 words, 134 characters.

## How it works

`main.py` writes that line to `/output/entry.txt`. It is deterministic
and offline — the review is a fixed string, with no randomness, no
network access, no timestamps, and no environment input — so every
run writes the exact same bytes.

```sh
python3 main.py
cat /output/entry.txt
```
