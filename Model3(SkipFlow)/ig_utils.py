from alibi.explainers import IntegratedGradients
from IPython.display import HTML
import matplotlib as mpl

def  hlstr(string, color='white'):
    """
    Return HTML markup highlighting text with the desired color.
    """
    return "<mark style=background-color:{}>{} </mark>".format(color, string)

def colorize(attrs, cmap='PiYG'):
    """
    Compute hex colors based on the attributions for a single instance.
    Uses a diverging colorscale by default and normalizes and scales
    the colormap so that colors are consistent with the attributions.
    """
    
    cmap_bound = np.abs(attrs).max()
    norm = mpl.colors.Normalize(vmin=-cmap_bound, vmax=cmap_bound)
    cmap = mpl.cm.get_cmap(cmap)

    # now compute hex values of colors
    colors = list(map(lambda x: mpl.colors.rgb2hex(cmap(norm(x))), attrs))
    return colors


def get_ig_model(model, layer_name = 'embedding', n_steps=50, batch_size=100, method="riemann_trapezoid"):
    ig  = IntegratedGradients(model,
                              layer=model.get_layer(layer_name),
                              n_steps=n_steps, 
                              method=method,
                              internal_batch_size=batch_size)
    return ig

def get_attributions(ig, v = x_val[0:1]):

  explanation = ig.explain(v, 
                         baselines=None)
  
  attrs = explanation.attributions
  attrs = attrs.sum(axis=2)
  
  return attrs[0]

