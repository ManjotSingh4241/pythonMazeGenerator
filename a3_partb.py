# Members
# 3.Abhi
# 1.Manjot Singh
# 2.Manak Preet Singh

from a2d import Graph


def minimum_spanning_tree(graph):

    emptarr = []
    shuru = 0
    apex = {shuru}
    corner = [(weight, shuru, to) for to, weight in graph.get_connected(shuru)]
    corner.sort()
    ex = set()
    num_verts = graph.num_verts()

    while True:
        while True:
            if not corner or len(apex) >= num_verts:
                break
            weight, frm, to = corner.pop(0)

            while True:
                while True:
                    while to not in apex and to not in ex:
                        apex.add(to)
                        emptarr.append((frm, to))
                        ex.add(to)

                        for to_next, weight_next in graph.get_connected(to):

                            while True:
                                while to_next in apex:
                                    break
                                for i in range(len(corner)):
                                      if corner[i][0] <= weight_next:
                                            continue
                                      corner.insert(i, (weight_next, to, to_next))
                                      break
                                else:
                                    corner.append((weight_next, to, to_next))
                                break

                        break
                    break
                break
        out = emptarr
        return out
