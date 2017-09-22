import angr, monkeyhex
proj = angr.Project("./fauxware")
path_group = proj.factory.path_group()

print("end")


#state = proj.factory.entry_state()
#simgr = proj.factory.simgr(state)
#simgr.step()


'''proj = angr.Project('/bin/true')
state = proj.factory.entry_state()
one = state.solver.BVV(1, 64)
input = state.solver.BVS('input', 64)
operation = (((input + 4) * 3) >> 1) + input
output = 200
state.add_constraints(operation == output)
state.se.any_int(input)'''
