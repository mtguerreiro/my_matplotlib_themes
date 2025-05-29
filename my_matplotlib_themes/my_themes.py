import matplotlib
import matplotlib.pyplot as plt

def _default():

    title_fontsize = 15
    legend_fontsize = 12
    label_fontsize = 14
    tick_fontsize = 14

    line_width = 1.75

    # Theme
    try:
        plt.style.use('seaborn-v0_8-bright')
    except:
        plt.style.use('seaborn-bright')

    # Fonts
    matplotlib.rcParams['mathtext.fontset'] = 'cm'
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['font.serif'] = 'CMU Serif'

    # Misc
    plt.rcParams['axes.unicode_minus'] = False

    # Grid
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.grid.which'] = 'major'
    plt.rcParams['grid.linestyle'] = ':'
    plt.rcParams['grid.alpha'] = 0.7

    # Ticks
    plt.rcParams['xtick.labelsize'] = tick_fontsize
    plt.rcParams['ytick.labelsize'] = tick_fontsize

    # Lines
    plt.rcParams['lines.linewidth'] = line_width

    # Labels
    plt.rcParams['axes.labelsize'] = label_fontsize

    # Legend
    plt.rcParams['legend.fontsize'] = legend_fontsize

    # Title
    plt.rcParams['figure.titlesize'] = title_fontsize
    plt.rcParams['axes.titlesize'] = title_fontsize
    #plt.rcParams['figure.titlesize'] = title_fontsize
    #plt.rcParams['figure.titleweight'] = title_fontsize

    # Tight layout
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['savefig.bbox'] = 'tight'


def default_tex_report():

    _default()


def default_beamer():

    _default()

    matplotlib.rcParams['mathtext.fontset'] = 'dejavusans'
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = 'CMU Sans Serif'

    
def default_ieee():

    _default()

    matplotlib.rcParams['font.serif'] = 'Times New Roman'
