# Python environment cmano


# https://wiki.baloogancampaign.com/index.php?title=Main_Page

from lua import CmdData

path = "."

cmd = CmdData(inpath=path, outpath=path, outfile='LuaCommands.txt')

# Read in all data
cmd.read('forces.csv') # The main forces
cmd.read('forces_dbids.csv')  # CommandPE database IDs that map to newly imported forces
cmd.read('sides.csv') # Defines the sides in a conflict, mapping a database side to a CommandPE game side
cmd.read('bases.csv') # A list of bases and other facilities from each side
cmd.read('aircraft.csv') # A list of aircraft to assign to bases

cmd.do_merges()  # Perform all table joins from the loaded data

# Build Lua commands for all entities. Aircraft must come last, since they need facilities
cmd.addFacilities()
cmd.addForces()
cmd.addAircraft()

# Write the buffer to a file, then copy the resulting Lua commands to the game console
cmd.write()