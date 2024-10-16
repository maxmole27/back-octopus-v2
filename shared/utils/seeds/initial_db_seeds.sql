/* inser 3 roles */
INSERT INTO public.roles
(id, "name", created_at, updated_at)
VALUES(nextval('roles_id_seq'::regclass), 'ADMIN', now(), now());

INSERT INTO public.roles
(id, "name", created_at, updated_at)
VALUES(nextval('roles_id_seq'::regclass), 'USER', now(), now());

INSERT INTO public.roles
(id, "name", created_at, updated_at)
VALUES(nextval('roles_id_seq'::regclass), 'MOD', now(), now());

/* insert 3 users */
INSERT INTO public.users
(id, "name", email, username, "password", created_at, updated_at, role_id)
VALUES(nextval('users_id_seq'::regclass), 'Max Joel', 'max@gmail.com', 'maxjoel10', 'PASSWORD_MUSTBE_BCRYPTED', now(), now(), 1);

INSERT INTO public.users
(id, "name", email, username, "password", created_at, updated_at, role_id)
VALUES(nextval('users_id_seq'::regclass), 'John Doe', 'asd@asd.com', 'johndoe', 'PASSWORD_MUSTBE_BCRYPTED', now(), now(), 1);

INSERT INTO public.users
(id, "name", email, username, "password", created_at, updated_at, role_id)
VALUES(nextval('users_id_seq'::regclass), 'Claude Monet', 'clau@monet.cl', 'claudemonet', 'PASSWORD_MUSTBE_BCRYPTED', now(), now(), 2);

/* insert 5 bookies POSTGRESQL */
INSERT INTO public.bookies
(id, "name", description, created_at, updated_at)
VALUES(nextval('bookies_id_seq'::regclass), 'Bet365', 'Bet365 is a world famous bookie', now(), now());

INSERT INTO public.bookies
(id, "name", description, created_at, updated_at)
VALUES(nextval('bookies_id_seq'::regclass), 'William Hill', 'William Hill is a world famous bookie', now(), now());

INSERT INTO public.bookies
(id, "name", description, created_at, updated_at)
VALUES(nextval('bookies_id_seq'::regclass), 'Betfair', 'Betfair is a world famous bookie', now(), now());

INSERT INTO public.bookies
(id, "name", description, created_at, updated_at)
VALUES(nextval('bookies_id_seq'::regclass), 'Ladbrokes', 'Ladbrokes is a world famous bookie', now(), now());

INSERT INTO public.bookies
(id, "name", description, created_at, updated_at)
VALUES(nextval('bookies_id_seq'::regclass), 'Paddy Power', 'Paddy Power is a world famous bookie', now(), now());


/* insert 5 sports POSTGRESQL */
INSERT INTO public.sports
(id, "name", description, created_at, updated_at)
VALUES(nextval('sports_id_seq'::regclass), 'Football', '', now(), now());

INSERT INTO public.sports
(id, "name", description, created_at, updated_at)
VALUES(nextval('sports_id_seq'::regclass), 'Basketball', '', now(), now());

INSERT INTO public.sports
(id, "name", description, created_at, updated_at)
VALUES(nextval('sports_id_seq'::regclass), 'Tennis', '', now(), now());

INSERT INTO public.sports
(id, "name", description, created_at, updated_at)
VALUES(nextval('sports_id_seq'::regclass), 'Baseball', '', now(), now());

INSERT INTO public.sports
(id, "name", description, created_at, updated_at)
VALUES(nextval('sports_id_seq'::regclass), 'Hockey', '', now(), now());


/* insert 5 Locations POSTGRESQL */

INSERT INTO public.locations
(id, "name", flag, code, is_country)
VALUES(nextval('locations_id_seq'::regclass), 'Unknown', 'FLAG_URL', 'UNK', false);

INSERT INTO public.locations
(id, "name", flag, code, is_country)
VALUES(nextval('locations_id_seq'::regclass), 'South America', 'FLAG_URL', 'SAM', false);

(id, "name", flag, code, is_country)
VALUES(nextval('locations_id_seq'::regclass), 'Europe', 'FLAG_URL', 'EUR', false);

INSERT INTO public.locations
(id, "name", flag, code, is_country)
VALUES(nextval('locations_id_seq'::regclass), 'Italy', 'FLAG_URL', 'ITA', true);

INSERT INTO public.locations
(id, "name", flag, code, is_country)
VALUES(nextval('locations_id_seq'::regclass), 'Spain', 'FLAG_URL', 'ESP', true);

INSERT INTO public.locations
(id, "name", flag, code, is_country)
VALUES(nextval('locations_id_seq'::regclass), 'England', 'FLAG_URL', 'ENG', true);

/* insert 5 PLAYERS OR TEAM POSTGRESQL */ 
INSERT INTO public.player_or_teams
(id, "name", alternative_name, alternative_name2, sport_id)
VALUES(nextval('player_or_teams_id_seq'::regclass), 'Casper Ruud', 'C Ruud', '', 3);

INSERT INTO public.player_or_teams
(id, "name", alternative_name, alternative_name2, sport_id)
VALUES(nextval('player_or_teams_id_seq'::regclass), 'Stefanos Tsitsipas', 'S Tsitsipas', '', 3);

INSERT INTO public.player_or_teams
(id, "name", alternative_name, alternative_name2, sport_id)
VALUES(nextval('player_or_teams_id_seq'::regclass), 'Los Angeles Lakers', 'LA Lakers', 'Lakers', 2);

INSERT INTO public.player_or_teams
(id, "name", alternative_name, alternative_name2, sport_id)
VALUES(nextval('player_or_teams_id_seq'::regclass), 'Real Madrid', 'Real Madrid CF', 'RMA', 1);

INSERT INTO public.player_or_teams
(id, "name", alternative_name, alternative_name2, sport_id)
VALUES(nextval('player_or_teams_id_seq'::regclass), 'Barcelona', 'FC Barcelona', 'BAR', 1);

/* insert 5 leagues or tournaments POSTGRESQL */

INSERT INTO public.league_or_tournaments
(id, "name", sport_id, location_id, image_url, alternative_name, alternative_name2, description)
VALUES(nextval('league_or_tournaments_id_seq'::regclass), 'English Premier League', 1, 5, '', 'EPL', '', '');

INSERT INTO public.league_or_tournaments
(id, "name", sport_id, location_id, image_url, alternative_name, alternative_name2, description)
VALUES(nextval('league_or_tournaments_id_seq'::regclass), 'La Liga', 1, 4, '', 'La Liga', '', '');

INSERT INTO public.league_or_tournaments
(id, "name", sport_id, location_id, image_url, alternative_name, alternative_name2, description)
VALUES(nextval('league_or_tournaments_id_seq'::regclass), 'NBA', 2, 1, '', 'NBA', '', '');

INSERT INTO public.league_or_tournaments
(id, "name", sport_id, location_id, image_url, alternative_name, alternative_name2, description)
VALUES(nextval('league_or_tournaments_id_seq'::regclass), 'Wimbledon', 3, 5, '', 'Wimbledon', '', '');

/* insert all bet status */

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Won', 'Winning bet');

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Lose', 'Losing bet');

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Pending', 'Bet is pending');

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Cancelled', 'Bet was cancelled');

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Void', 'Bet was voided');

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Half Win', 'Half win and half void');

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Half Loss', 'Half lost and half void');

INSERT INTO public.bet_status
(id, "name", description)
VALUES(nextval('bet_status_id_seq'::regclass), 'Unknown', 'Unknown bet status');



