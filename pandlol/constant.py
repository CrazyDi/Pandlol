from pandas import DataFrame


url_versions = "https://ddragon.leagueoflegends.com/api/versions.json"
url_champions = "http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json"
url_champions_full = "http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/championFull.json"

stat = DataFrame({"stat_code": list(range(1, 21)),
                  "stat_name": [
                      'hp', 'hpperlevel', 'mp', 'mpperlevel', 'movespeed', 'armor',
                      'armorperlevel', 'spellblock', 'spellblockperlevel', 'attackrange',
                      'hpregen', 'hpregenperlevel', 'mpregen', 'mpregenperlevel', 'crit',
                      'critperlevel', 'attackdamage', 'attackdamageperlevel',
                      'attackspeedperlevel', 'attackspeed']})
