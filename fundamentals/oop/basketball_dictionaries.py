players = [ #list of player dictionaries
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

############################################ CHALLENGE 1 ############################################
class Player:
    def __init__(self, player): #removed individual args. inserted dict variable
        self.name = player["name"] #assigned all Player object attributes by using dictionary keys
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    ############### NINJA BONUS ###############
    @classmethod
    def get_team(cls, team_list):
        team = []
        for player in team_list:
            team.append(cls(player))
        return team

#testing class method with these lines
cls_method_team = Player.get_team(players) 
print(len(cls_method_team))

############################################ CHALLENGE 2 ############################################
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

############################################ CHALLENGE 3 ############################################
new_team = []
for player in players:
    new_team.append(Player(player))
