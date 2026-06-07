# autosens
automatic sensitivity converter for games

this is a proof of concept.

problem: games always use different sensitivity scalers. in one game, my sensitivity (sens) could be 1, and in another I might need a sens of 30 to get the same speed. calculators/converters exist, but I need to find one online each time I play a new game and remember/check on another game's sensitivity to convert from.

plan: an app that stores one game's sensitivity as a base value, and sets new games' sensitivities automatically based on this, to match the same mouse speed in all games (this could also have an override for any games where a different sens is desired)

method: edit the game data files, e.g. CVARS, XML, JSON files. automatically edit the mouse sensitivity setting for the games via a script.