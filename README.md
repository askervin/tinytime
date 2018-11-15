# tinytime
Present time and date with six digits and do other conversions

Examples
--------

- ``tinytime epoch`` once printed ``4s5DW1``, that is an epoch timestamp in tinytime base 60 format.

- ``tinytime 4s5DW1`` prints ``2018-04-24 16:32:01``, if local time zone is +0300 to UTC.

- ``tinytime 4s5DXW-4s1BXr`` prints time difference: ``4d 1h 59m 39s``

Timestamp explained
-------------------

```
4s5DW1
^^^^^^
|||||\.. seconds, symbols 0..9A..Za..x, x equals 59.
||||\... minutes, symbols 0..9A..Za..x
|||\.... hours, symbols 0..9A..N, N equals 23.
\\\..... days since 1970-01-01, symbols 0..9A..Za..x
```

Where to use it
---------------

- Log timestamps

- Version numbers

- In your prompt: ``export PS1="\$(tinytime epoch) $PS1"``

Example: show previous command run time in prompt
-------------------------------------------------

At the end of ``.bashrc``:
```
function tinytime_command_timer() {
    TINYTIME_LAST_CMD=$TINYTIME_RUN_CMD
    TINYTIME_RUN_CMD=$(HISTTIMEFORMAT= history 1);
    if [ "$TINYTIME_LAST_CMD" != "$TINYTIME_RUN_CMD" ]; then
        TINYTIME_RUN_START=$(tinytime epoch);
    fi
}
PS1='$(tinytime $(tinytime epoch)-$TINYTIME_RUN_START) $(tinytime epoch) '$PS1
TINYTIME_RUN_START=$(tinytime epoch)
trap tinytime_command_timer DEBUG
```
