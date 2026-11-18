# Beginner's guide to Blood on the Clocktower custom scripts

> 출처: Not Quite Tangible (2024-07-09) — https://notquitetangible.blogspot.com/2024/07/clocktower-custom-scripts.html
> 커스텀 스크립트 설계 가이드 영어 원문. PDF에서 글자만 뽑아 옮겼으므로 원문 서식·링크는 위 주소에서 확인한다.

---

Not Quite Tangible
09 July 2024

Beginner's guide to Blood on the Clocktower custom
scripts
This is a guide for crafting custom scripts for the social deduction game Blood on the Clocktower.
The game's core editions – Trouble Brewing, Bad Moon Rising and Sects & Violets – are well-tested
and meticulously-balanced game-theoretic ecosystems, but the game's enormous cast of
characters and complex emergent gameplay interactions create an irresistible temptation to
experiment with new combinations of bluffers and puzzle-solvers. This post, which draws heavily on
the wisdom already shared within the community, provides a checklist of principles to keep in mind.
Even if you aren't in the business of making custom scripts, unpacking exactly what goes into a
great Blood on the Clocktower script is interesting from a game design perspective, and this post
will highlight some of the less obvious features that make Clocktower's core editions work so well.
If you have no idea what I'm talking about, introductions to the game can be found here (official
website) and here (video).

## Outline
The rest of this post consists of ten guidelines, listed in roughly descending order of priority. Links to
further resources are provided at the end.
1. Figure out the basics
2. Include misinformation
3. Conceal the outsider count
4. Conceal which Demon is in play
5. Avoid good characters who are too easy to confirm
6. Give the good team reasons to be secretive
7. Give the evil team an escape hatch
8. Aim for similar minion "loudness"
9. Consider using Fabled
10. Consider starting Teensy
Two things are essential to remember. First, these are guidelines, not commandments. There will
certainly be occasions where you decide it's right to do something differently.
Second, the best way to evaluate your script is by playing it! Unexpected interactions between
characters are a vital part of Blood on the Clocktower, and giving players creative opportunities to
exploit these interactions will make the game all the more fun, but often the only way to discover
these interactions and gauge their impact on the player experience will be to watch them show up
organically when your script is played.

## 1. Figure out the basics
So, you have your cool idea for a script. Maybe there's a gameplay theme you want to focus on, or
a couple of characters you really like and want to include.
The best place to start is the Script Tool from the official Clocktower site. As well as making it easy
to add and remove characters, the Script Tool will automatically figure out night order, flag jinxed
characters and generate a printable PDF to share with players.
Make sure your script has the minimum number of characters of each type. For a standard game
this is at least 13 Townsfolk, 4 Outsiders, 4 Minions and at least 1 Demon. A lot of the time you'll be
working from the bottom upwards, starting with your Demons and building the remaining characters
around them.
Among your Townsfolk, make sure there's at least a few that receive information. It's recommended
to list Townsfolk in "Steven-approved order", which groups together characters according to when
their ability takes effect (again, this is something the official Script Tool can automate, using the
"automatic sorting" button on the right).

## 2. Include misinformation
A crucial goal for the good team is separating true information from misinformation. If the good team
have no reason to doubt any of the information they are given, it will usually be too difficult for the
evil team to win.
Misinformation can be created consciously by the evil team (e.g. through the Poisoner and Pukka's
targeted poisoning) or exist passively as a result of characters' abilities (e.g. Drunk or Vortox). If in
doubt, it's good to include both types of misinformation sources.

Madness abilities (like Mutant and Cerenovus) are a less effective source of misinformation.
Although they may encourage the good team to doubt each other, keep in mind that madness does
not cause players to doubt their own information, and players can always break madness if they
want to (and they are happy to face the consequences).

## 3. Conceal the outsider count
By default, the number of Outsiders in the game is determined by the overall number of players. But
if the good team know exactly how many Outsiders should be in play, it will be much harder for
players on the evil team to bluff as an Outsider. It will also make it easier for Outsiders who believe
they are other characters (e.g. Drunk and Lunatic) to figure out their true role.
There are two ways of avoiding this: either include characters that directly manipulate the Outsider
count (especially evil characters, since they won't make themselves public), or Outsiders who are
less likely to make themselves known to the good team (because of madness, because they don't
know they're Outsiders, or because they may change teams). The former type of obfuscation is
generally most effective, but if in doubt, it's good to include both (like in the three base scripts).

## 4. Conceal which Demon is in play
If there is more than one Demon on the script, part of the puzzle for the good team is working out
which Demon is in play. Make sure that this is indeed a puzzle! Be careful with Demons which
cause more than one death per night, since they will clearly signal their presence unless there are
other sources of death at night.
On some scripts (including the classic Trouble Brewing) there is only one Demon on the script. For
these games, the good team will not need to spend any effort figuring out which Demon is in play.
Keep in mind that some Demons (like the Vortox and Legion) work best when it's not guaranteed
they are in play, letting them instil paranoia in the good team.

## 5. Avoid good characters who are too easy to confirm
In general, games are most fun when no good player can be completely trusted. To support this, it's
worth having ways for the evil team to plausibly look like any good character on the script (or as
many as possible).
For "information" roles, this is usually not much of a concern: for example, any evil player can bluff
as a Clockmaker and invent a number (although extremely info-heavy characters like Undertaker
are hard to bluff without an info-heavy Minion like Spy or Widow).
For "power" abilities which kill, protect or resurrect, the consequences are much more visible and it's
harder for the evil team to bluff as them without extra support. For example, the Professor's ability to
resurrect another character is almost impossible for the evil team to fake unless they have a
Shabaloth on their team (and even then, it will usually require coordination with the storyteller or
very good luck). The Devil's Advocate, an evil character that can protect others from death by
execution, is a versatile mechanism for the evil team to bluff as a protection role like Tea Lady,
Pacifist or Sailor.

Another interesting option is to include ways of generating evil characters with Townsfolk abilities.
With a Bounty Hunter, Pit-Hag or Boffin on the script, even a player who can confirm they have a
Townsfolk ability won't be guaranteed to be on the good team.

## 6. Give the good team reasons to be secretive
In a typical social deduction game, the good team will tend to be honest and the evil team will tend
to lie. But you can make games much more exciting if the good team is incentivised to conceal
some of their information.
On the one hand, good team secrecy makes the game less of an uphill battle for the evil team: if
every good player thinks it's best to publicly state their role on day one, it will be significantly harder
for the evil team to bluff. I would also argue that good team secrecy makes the game more fun:

players who enjoy detective work will be able to do it even if they are assigned the evil team, and
players who enjoy deception will have more opportunity to do it even if they are on the good team.
Some good characters (like the Damsel, Pixie and Magician) explicitly want to hide their role.
Having these characters on the script will nudge the whole good team towards concealing their
roles, so that they can protect the members of their team who really need to stay under the radar.
You can also gently encourage the good team to be secretive by including a mix of good characters
who want to get killed at night and characters who want to stay alive. If your good characters are
taken from across the spectrum pictured below, they will not want to be too open about their roles,
in the hope that the Demon will target the wrong player at night.

One last factor to think about is how good team secrecy affects the relative strength of evil
characters. If your good team are encouraged to keep quiet about their roles, evil information
characters (like Spy and Widow) become much more powerful, whereas characters that need
information to work effectively (like Poisoner and Pit-Hag) are weaker.

## 7. Give the evil team an escape hatch
A loss through bad luck tends to happen more often for the evil team than for the good team. By
default, the good team only needs one lucky execution to win the game. To balance this out,
consider including an "escape hatch" which helps the evil team get back on their feet if the game is
going badly. Another gameplay function served by many escape hatches (including Imp, Zombuul
and Fang Gu) is giving the good team more reason to suspect that a dead player is evil, sowing
extra distrust.
Escape hatches can take a number of different forms. The most obvious are abilities letting a
Demon jump to another character if they're attracting too much suspicion, or letting the game
continue after the Demon is executed. Each of the three base scripts includes at least two escape
hatches.

## 8. Aim for similar minion "loudness"
Some minions are "loud", meaning that the good team will learn quickly that they are in play. Others
are "quiet", affecting the game in more subtle ways. A quiet minion tends not to work as well on a
script where other minions are loud: the good team will be able to work out they are in play by
process of elimination (having not seen the obvious "tells" for the loud minions on the script),
making it hard for the quiet minion to influence the game discreetly.
A good approach is to have all the minions be a roughly similar level of loudness: all quiet (like in
Trouble Brewing), all loud (like in Sects & Violets) or all in the middle (like in Bad Moon Rising).

For a more comprehensive guide to loudness, see this Substack post by Hystrex.

## 9. Consider using Fabled
Fabled, while officially called "characters", don't have any agency and aren't controlled by any
player. They are best thought of as flavourful ways of tweaking the rules of your game.
Duchess, Fibbin, Sentinel and Spirit of Ivory are specifically designed to help balance custom
scripts when it's not possible to do so by adding or removing (non-Fabled) characters. Other Fabled
don't have script balancing as their principal goal, but sometimes appear on custom scripts to make
games more interesting, such as Revolutionary on Comrade Demon or Doomsayer on Race to the
Bottom.

The Djinn is a special Fabled which adds new rules to amend the interaction between two
characters on a script. Officially, the two characters are said to be "jinxed" when unpatched, but
you'll usually see the community instead use "jinx" to refer to the patch itself (which is the approach
used in the rest of this post).
There's a lot of variation in how jinxes work. In the most extreme case, so-called "hate jinxes"
declare that two characters cannot be in play at the same time (this applies, for example, to Spy and
Heretic). At the other end of the spectrum, there are characters that work perfectly well together, but
a jinx exists allowing them to interact in an interesting way (such as the Mathematician seeing the
Lunatic malfunction, or the Cerenovus making a player mad they are the Goblin).
Some people are anxious about including jinxed characters on custom scripts, out of a fear that
jinxes are just band-aids to stop poorly-built scripts from completely breaking. This is generally a
mischaracterisation: jinxes are designed to cultivate fun and interesting character interactions and
are worth embracing.
That said, avoid overloading players with too much rules complexity, and make sure that any jinxes
on the script are clearly explained before the game starts (even if the jinxed characters aren't in
play). Losing because you didn't understand all the fine print is never fun!
There is a lot more that can be said about the how the possibility of extra evil characters affects a
script's balance and the places where the Spirit of Ivory is appropriate or inappropriate. This blog
post contains some helpful analysis.

## 10. Consider starting Teensy
"Teensyville" games, which have 5 or 6 players, use their own type of script with a smaller pool of
characters (6 Townsfolk, 2 Outsiders, 2 Minions and 1-2 Demons). Steven Medway, creator of Blood

on the Clocktower, suggests that Teensyville scripts are a perfect starting point for new script
designers, quicker to assemble, faster to playtest and easier to focus around a central theme.

Pictured above is No Greater Joy, the archetypal entry-level Teensyville script, illustrating all the
principles described so far:
There is a source of misinformation (Drunk);
There is outsider count manipulation (Baron);
All Townsfolk are information characters who are easy for the evil team to bluff (this is
especially important in Teensyville games where the evil team aren't given any not-in-play
characters to bluff as);
There are good characters who want to stay alive (Empath, Chambermaid and especially
Klutz) and a character who wants to get killed at night (Sage), encouraging some good-team
secrecy;
There are two escape hatches (Imp and Scarlet Woman); and
The two Minions are similar in terms of loudness (both very quiet).

## Further resources
Recommended custom scripts
The official Blood on the Clocktower site has a regularly-updated page listing some of the
team's favourite custom scripts. An archive of scripts which have historically been featured
on this page is maintained here on Reddit and here as a Google doc.
AdmiralGT's BotC Scripts is a large searchable database of custom scripts.
The Carousel Script Collection is an officially-curated set of custom scripts designed to
curate the experimental characters released as the "Carousel" token pack.
The Streamer Stack is a collection of popular custom scripts from streamers and their
communities.
Bakery by the Clocktower includes a curated list of well-known scripts.
Zets has assembled a list of neat, balanced custom scripts, available on Imgur.
Scriptbuilding guides
This Reddit comment by official storyteller Ben Burns covers six "must-haves" for custom
scripts.

"The Teensyville Fair" is a Tumblr post by BotC creator Steven Medway with advice on
building Teensyville scripts. Much of the advice is also applicable to full-size scripts.
Angelus Morningstar's Ravenswood Bluff site includes an excellent scriptbuilding guide as
well as a collection of custom scripts.
Script Tease is a podcast series specifically focused on scriptbuilding. The first episode looks
at features common to the three base scripts as a guide for what to include in custom scripts.
Grim Scenarios is a general BotC podcast series which often discusses scriptbuilding.
Episode 24b, for example, discusses some of the challenges that arise when mixing
characters from the three base scripts. The podcast creators also maintain a list of
recommended custom scripts, available here and here and a "Script Building Compendium"
available here.
Discussion forums
The BotC subreddit has a "Scripts" flair. You can search for this flair to find other custom
scripts, or tag a post with this flair to get feedback on your own script.
The unofficial BotC discord server has a channel for custom script discussion.
Not Quite Tangible at 17:05
