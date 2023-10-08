# Python environment cmano

'''
References

http://commandlua.github.io/
http://commandlua.github.io/#Functions
'''

class ScenarioBuilder:
    def __init__(self):
        print("Scenario Builder initialized")

    def add_unit(self, name, unittype, lat, lng, side, dbid=2023):
        lua_add_unit = "ScenEdit_AddUnit({side='%s', type='%s', name=\"%s\", dbid=%u, latitude='%f', longitude='%f'})\n" % (side, unittype, name, dbid, lat, lng)