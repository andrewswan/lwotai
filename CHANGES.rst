=========
Changelog
=========

Version 1.11082014.1 (by sgwestrip)
===================================

Changed wording for Jihadist Ideology choices. The wording is now as per the rulebook.
Added: release number displays when you first run the program.

Version 1.06082014.2 (by ragam)
===============================

Fix: cards #84/85 will now make you Shift Ally to Neutral, if possible.
Fix: card #58 will now correctly Disrupt cadres if the event is in play

Version 1.04082014.1 (by sgwestrip)
===================================

Add: new Jihadist Ideology (9.7) Coherent. This was added to the rules after the initial printing.
Fix: card #75 now displays 'Remove card from game' when it is played for the event.
Fix: numerous typos
Fix: remove all "Jihadist Activity Phase finished, enter plot command." as this is incorrect. It should always be done after the 2nd US Activity Phase.

Version 1.06162015.1
====================
1. Made use of CTR consistent - was adding CRT but testing for CTR (reported by Morten Kristensen)

Version 1.20150312.1
====================
1. Fixed missing line for card 102 (reported by Thomas Chipman)

Version 1.20150303.1
====================
1. Prevent double processing when major jihad failure sets besieged status (reported by Magnus Kvevlander)

Version 1.20150131.1
====================
1. Fixed spelling of besieged in Country class
2. Added untested countries with data to 'status' command so that 'status' can be used to reconstruct the board
3. Fixed 'help dep'
4. Added valid global markers, country markers and lapsing markers for use by 'adjust' command
5. Added 'adjust' command for ideology, prestige, funding, event markers, lapsing markers and country data
6. Additional changes for multiple aid markers when adding or removing
7. In plot resolution, remove one aid for each successful roll
8. In WoI roll adjustment, add 1 to modifiers for each aid marker
9. Ignore "The door of Itjihad is closed" when checking playable if playing as US (reported by Dave Horn)
10. Changed removeCell to remove sleeper then Sadr then active if playing as US; but active then sleeper then Sadr if Jihadist
11. Fixed test for infectious ideology when setting difficulty
12. Added 'summary' command to display state of each track
13. Changed message if no Islamist Rule countries at 'turn'
14. Changed message when card 1 event activated

See GitHub for changes submitted via pull request, e.g. by andrewswan.
