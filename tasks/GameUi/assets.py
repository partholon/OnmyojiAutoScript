from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by module/dev_tools/assets_extract.py.
# Don't modify it manually.
class GameUiAssets: 


	# Image Rule Assets
	# description 
	I_CHECK_MAIN = RuleImage(roi_front=(54,228,38,37), roi_back=(30,205,1033,96), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_main.png")
	# description 
	I_MAIN_GOTO_EXPLORATION = RuleImage(roi_front=(493,116,45,75), roi_back=(243,100,933,211), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_exploration.png")
	# description 
	I_CHECK_EXPLORATION = RuleImage(roi_front=(1130,120,61,55), roi_back=(1130,120,61,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_exploration.png")
	# description 
	I_EXPLORATION_GOTO_AWAKE_ZONE = RuleImage(roi_front=(50,637,57,61), roi_back=(50,637,57,61), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_awake_zone.png")
	# description 
	I_EXPLORATION_GOTO_SOUL_ZONE = RuleImage(roi_front=(151,637,55,55), roi_back=(151,637,55,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_soul_zone.png")
	# description 
	I_EXPLORATION_GOTO_REALM_RAID = RuleImage(roi_front=(245,638,67,48), roi_back=(245,638,67,48), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_realm_raid.png")
	# 前往御灵 
	I_EXPLORATION_GOTO_GORYOU_REALM = RuleImage(roi_front=(343,629,60,67), roi_back=(343,629,60,67), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_goryou_realm.png")
	# 式神委派 
	I_EXPLORATION_GOTO_DELEGATION = RuleImage(roi_front=(445,638,60,50), roi_back=(445,638,60,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_delegation.png")
	# 秘闻 
	I_EXPLORATION_GOTO_SECRET_ZONES = RuleImage(roi_front=(542,645,61,55), roi_back=(542,645,61,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_secret_zones.png")
	# 地狱鬼王 
	I_EXPLORATION_GOTO_AREA_BOSS = RuleImage(roi_front=(640,638,51,45), roi_back=(640,638,51,45), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_area_boss.png")
	# 平安奇谭 
	I_EXPLORATION_GOTO_HEIAN_KITAN = RuleImage(roi_front=(739,643,52,44), roi_back=(739,643,52,44), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_heian_kitan.png")
	# 六道之门 
	I_EXPLORATION_GOTO_SIX_GATES = RuleImage(roi_front=(834,641,60,49), roi_back=(834,641,60,49), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_six_gates.png")
	# 器灵 
	I_EXPLORATION_GOTO_BONDLING_FAIRYLAND = RuleImage(roi_front=(937,639,61,54), roi_back=(937,639,61,54), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_exploration_goto_bondling_fairyland.png")
	# description 
	I_BACK_BLUE = RuleImage(roi_front=(32,37,54,52), roi_back=(3,2,130,114), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_blue.png")
	# description 
	I_CHECK_AWAKE = RuleImage(roi_front=(376,565,73,82), roi_back=(376,565,73,82), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_awake.png")
	# description 
	I_CHECK_SOUL_ZONES = RuleImage(roi_front=(49,105,298,405), roi_back=(49,105,298,405), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_soul_zones.png")
	# description 
	I_CHECK_REALM_RAID = RuleImage(roi_front=(123,632,57,55), roi_back=(123,632,57,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_realm_raid.png")
	# description 
	I_CHECK_GORYOU = RuleImage(roi_front=(881,17,30,39), roi_back=(881,17,30,39), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_goryou.png")
	# description 
	I_CHECK_DELEGATION = RuleImage(roi_front=(839,132,49,45), roi_back=(839,132,49,45), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_delegation.png")
	# description 
	I_CHECK_SECRET_ZONES = RuleImage(roi_front=(1145,592,110,119), roi_back=(1145,592,110,119), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_secret_zones.png")
	# description 
	I_CHECK_AREA_BOSS = RuleImage(roi_front=(41,637,65,62), roi_back=(41,637,65,62), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_area_boss.png")
	# description 
	I_CHECK_HEIAN_KITAN = RuleImage(roi_front=(27,48,47,39), roi_back=(27,48,47,39), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_heian_kitan.png")
	# description 
	I_CHECK_SIX_GATES = RuleImage(roi_front=(1174,621,55,44), roi_back=(1174,621,55,44), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_six_gates.png")
	# description 
	I_CHECK_BONDLING_FAIRYLAND = RuleImage(roi_front=(614,660,56,49), roi_back=(614,660,56,49), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_bondling_fairyland.png")
	# description 
	I_SIX_GATES_GOTO_EXPLORATION = RuleImage(roi_front=(18,19,52,55), roi_back=(18,19,52,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_six_gates_goto_exploration.png")
	# description 
	I_BONDLING_GOTO_EXPLORATION = RuleImage(roi_front=(20,13,60,59), roi_back=(20,13,60,59), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_bondling_goto_exploration.png")


	# Image Rule Assets
	# description 
	I_MAIN_GOTO_TOWN = RuleImage(roi_front=(706,249,61,57), roi_back=(200,120,951,298), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_town.png")
	# description 
	I_CHECK_TOWN = RuleImage(roi_front=(1034,94,100,100), roi_back=(1034,94,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_town.png")
	# description 
	I_TOWN_GOTO_MAIN = RuleImage(roi_front=(1017,231,78,73), roi_back=(302,216,868,127), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_main.png")
	# description 
	I_TOWN_GOTO_DUEL = RuleImage(roi_front=(756,142,48,68), roi_back=(357,126,657,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_duel.png")
	# description 
	I_TOWN_GOTO_DEMON_ENCOUNTER = RuleImage(roi_front=(617,135,51,75), roi_back=(232,121,873,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_demon_encounter.png")
	# description 
	I_TOWN_GOTO_HUNT = RuleImage(roi_front=(475,138,46,69), roi_back=(275,122,520,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_hunt.png")
	# 协同对弈 
	I_TOWN_GOTO_DRAFT_DUEL = RuleImage(roi_front=(335,159,55,72), roi_back=(170,145,567,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_draft_duel.png")
	# 百鬼奕 
	I_TOWN_GOTO_HYAKKISEN = RuleImage(roi_front=(192,145,48,67), roi_back=(86,130,447,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_town_goto_hyakkisen.png")
	# description 
	I_CHECK_DUEL = RuleImage(roi_front=(1045,610,50,53), roi_back=(1018,579,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_duel.png")
	# description 
	I_CHECK_DEMON_ENCOUNTER = RuleImage(roi_front=(26,658,42,43), roi_back=(2,619,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_demon_encounter.png")
	# description 
	I_CHECK_HUNT = RuleImage(roi_front=(1071,605,81,85), roi_back=(1026,558,152,156), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_hunt.png")
	# description 
	I_CHECK_HYAKKISEN = RuleImage(roi_front=(1014,607,53,55), roi_back=(986,587,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_hyakkisen.png")
	# description 
	I_CHECK_DRAFT_DUEL = RuleImage(roi_front=(1051,612,56,58), roi_back=(1029,594,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_draft_duel.png")
	# description 
	I_BACK_YOLLOW = RuleImage(roi_front=(24,16,48,55), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_yollow.png")
	# description 
	I_DEMON_ENCOUNTER_GOTO_TOWN = RuleImage(roi_front=(28,20,56,52), roi_back=(3,4,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_demon_encounter_goto_town.png")


	# Image Rule Assets
	# 式神录 
	I_MAIN_GOTO_SHIKIGAMI_RECORDS = RuleImage(roi_front=(1097,612,56,64), roi_back=(1097,612,56,64), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_shikigami_records.png")
	# description 
	I_MAIN_GOTO_ONMYODO = RuleImage(roi_front=(992,614,51,60), roi_back=(992,614,51,60), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_onmyodo.png")
	# description 
	I_MAIN_GOTO_FRIENDS = RuleImage(roi_front=(878,623,55,55), roi_back=(878,623,55,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_friends.png")
	# description 
	I_MAIN_GOTO_DAILY = RuleImage(roi_front=(769,623,52,54), roi_back=(769,623,52,54), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_daily.png")
	# description 
	I_MAIN_GOTO_MALL = RuleImage(roi_front=(657,624,47,52), roi_back=(657,624,47,52), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_mall.png")
	# description 
	I_MAIN_GOTO_GUILD = RuleImage(roi_front=(540,611,50,54), roi_back=(540,611,50,54), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_guild.png")
	# description 
	I_MAIN_GOTO_TEAM = RuleImage(roi_front=(429,622,53,51), roi_back=(429,622,53,51), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_team.png")
	# description 
	I_MAIN_GOTO_COLLECTION = RuleImage(roi_front=(92,611,51,64), roi_back=(92,611,51,64), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_collection.png")
	# description 
	I_CHECK_RECORDS = RuleImage(roi_front=(269,71,55,50), roi_back=(269,71,55,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_records.png")
	# description 
	I_CHECK_ONMYODO = RuleImage(roi_front=(1166,117,84,547), roi_back=(1166,117,84,547), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_onmyodo.png")
	# description 
	I_CHECK_FRIENDS = RuleImage(roi_front=(1011,592,133,60), roi_back=(1011,592,133,60), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_friends.png")
	# description 
	I_CHECK_DAILY = RuleImage(roi_front=(28,510,69,87), roi_back=(28,510,69,87), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_daily.png")
	# description 
	I_CHECK_MALL = RuleImage(roi_front=(7,503,100,100), roi_back=(7,503,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_mall.png")
	# description 
	I_CHECK_GUILD = RuleImage(roi_front=(1072,630,49,46), roi_back=(1072,630,49,46), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_guild.png")
	# description 
	I_CHECK_TEAM = RuleImage(roi_front=(1209,108,41,119), roi_back=(1209,108,41,119), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_team.png")
	# description 
	I_CHECK_COLLECTION = RuleImage(roi_front=(471,618,100,100), roi_back=(471,618,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_collection.png")
	# description 
	I_BACK_Y = RuleImage(roi_front=(15,4,57,52), roi_back=(1,2,100,91), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_y.png")
	# description 
	I_BACK_MALL = RuleImage(roi_front=(28,33,50,51), roi_back=(28,33,50,51), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_mall.png")
	# description 
	I_BACK_FRIENDS = RuleImage(roi_front=(1152,87,53,52), roi_back=(1152,87,53,52), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_friends.png")
	# description 
	I_BACK_DAILY = RuleImage(roi_front=(33,13,39,50), roi_back=(33,13,39,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_back_daily.png")
	# description 
	I_NEW = RuleImage(roi_front=(0,0,100,100), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/image_name.png")


	# Image Rule Assets
	# description 
	I_MAIN_GOTO_SUMMON = RuleImage(roi_front=(1073,174,57,65), roi_back=(571,153,586,124), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_main_goto_summon.png")
	# description 
	I_SUMMON_GOTO_MAIN = RuleImage(roi_front=(27,5,49,51), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_summon_goto_main.png")
	# description 
	I_CHECK_SUMMON = RuleImage(roi_front=(581,594,68,66), roi_back=(316,528,594,174), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_check_summon.png")
	# 就是一个红叉 
	I_REALM_RAID_GOTO_EXPLORATION = RuleImage(roi_front=(1192,107,36,43), roi_back=(1192,107,36,43), threshold=0.8, method="Template matching", file="./tasks/GameUi/page/page_realm_raid_goto_exploration.png")


	# Image Rule Assets
	# 左上角蓝色的返回 
	I_BACK_BL = RuleImage(roi_front=(32,31,50,53), roi_back=(1,2,139,120), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_back_blue.png")
	# 式神录 
	I_HOME_SHIKIKAMI = RuleImage(roi_front=(1092,611,73,41), roi_back=(1092,611,73,41), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_shikikami.png")
	# 阴阳术 
	I_HOME_OMNYOUJI = RuleImage(roi_front=(989,613,59,58), roi_back=(989,613,59,58), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_omnyouji.png")
	# description 
	I_HOME_FRIEND = RuleImage(roi_front=(876,619,60,53), roi_back=(876,619,60,53), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_friend.png")
	# 花合战 
	I_HOME_TSK = RuleImage(roi_front=(764,608,66,56), roi_back=(764,608,66,56), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_tsk.png")
	# 商店 
	I_HOME_MALL = RuleImage(roi_front=(654,620,51,55), roi_back=(654,620,51,55), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_mall.png")
	# 阴阳寮 
	I_HOME_GUILD = RuleImage(roi_front=(540,607,53,50), roi_back=(540,607,53,50), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_guild.png")
	# 组队 
	I_HOME_TEAM = RuleImage(roi_front=(430,616,49,61), roi_back=(430,616,49,61), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_team.png")
	# 同心队 
	I_HOME_CONCENTRIC_TEAM = RuleImage(roi_front=(310,618,67,60), roi_back=(310,618,67,60), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_concentric_team.png")
	# 珍旅居 
	I_HOME_HELP = RuleImage(roi_front=(201,617,56,57), roi_back=(201,617,56,57), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_help.png")
	# 图鉴 
	I_HOME_COLLECT = RuleImage(roi_front=(92,607,48,74), roi_back=(92,607,48,74), threshold=0.8, method="Template matching", file="./tasks/GameUi/res/res_home_collect.png")


	# Ocr Rule Assets
	# 庭院到探索 
	O_HOME_EXPLORE = RuleOcr(roi=(310,105,858,194), area=(0,0,100,100), mode="Full", method="Default", keyword="探索", name="home_explore")
	# Ocr-description 
	O_NEW = RuleOcr(roi=(0,0,100,100), area=(0,0,100,100), mode="Single", method="Default", keyword="", name="new")


