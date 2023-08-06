import matplotlib.pyplot as plt
import math as m


atomList = []
bondList = []
def singleBond():
    plt.plot(
        [float(atomList[int(bondList[-1][3]) - 1][3]), float(atomList[int(bondList[-1][4]) - 1][3])],
        [float(atomList[int(bondList[-1][3]) - 1][4]), float(atomList[int(bondList[-1][4]) - 1][4])],
        color='dimgrey', zorder=1, linewidth=2)


def doubleBond():
    # float result = (
    #     Mathf.Atan((mousePos.x - startAtom.transform.position.x) / ((mousePos.y - startAtom.transform.position.y))));
    #
    # line1.SetPosition(0, startAtom.transform.position + new
    # Vector3(distance * Mathf.Cos(result), distance * Mathf.Sin(result + (45 * Mathf.PI)), 1
    # f));
    # line2.SetPosition(0, startAtom.transform.position + new
    # Vector3(distance * Mathf.Cos(result + (45 * Mathf.PI)), distance * Mathf.Sin(result), 1
    # f));

    result = m.atan(
        ((float(atomList[int(bondList[-1][4]) - 1][3])) - (float(atomList[int(bondList[-1][3]) - 1][3]))) / (
                    (float(atomList[int(bondList[-1][4]) - 1][4])) - (float(atomList[int(bondList[-1][3]) - 1][4]))))
    # print(result)
    distance = 0.1
    plt.plot([float(atomList[int(bondList[-1][3]) - 1][3]) + (distance * m.cos(result)),
              float(atomList[int(bondList[-1][4]) - 1][3]) + (distance * m.cos(result))],
             [float(atomList[int(bondList[-1][3]) - 1][4]) + (distance * m.sin(result + (45 * m.pi))),
              float(atomList[int(bondList[-1][4]) - 1][4]) + (distance * m.sin(result + (45 * m.pi)))], zorder=1,
             color='dimgrey', linewidth=2)

    plt.plot([float(atomList[int(bondList[-1][3]) - 1][3]) + (distance * m.cos(result + (45 * m.pi))),
              float(atomList[int(bondList[-1][4]) - 1][3]) + (distance * m.cos(result + (45 * m.pi)))],
             [float(atomList[int(bondList[-1][3]) - 1][4]) + (distance * m.sin(result)),
              float(atomList[int(bondList[-1][4]) - 1][4]) + (distance * m.sin(result))], color='dimgrey',
             zorder=1,
             linewidth=2)


def tripleBond():
    pass

