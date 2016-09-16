def convert_ipynb(infile,outfile):
    nb_start = '''{
     "cells": [
      {
       "cell_type": "code",
       "execution_count": null,
       "metadata": {
        "collapsed": true
       },
       "outputs": [],
       "source": [
        "import IPython.core.display as di\\n",
        "\\n",
        "# This line will hide code by default when the notebook is exported as HTML\\n",
        "di.display_html('<script>jQuery(function() {if (jQuery(\\"body.notebook_app\\").length == 0) { jQuery(\\".input_area\\").toggle(); jQuery(\\".prompt\\").toggle();}});</script>', raw=True)\\n",
        "\\n",
        "# This line will add a button to toggle visibility of code blocks, for use with the HTML export version\\n",
        "di.display_html(\'''<button onclick=\\"jQuery('.input_area').toggle(); jQuery('.prompt').toggle();\\">Toggle code</button>\''', raw=True)"
       ]
      },

      {
       "cell_type": "code",
       "execution_count": null,
       "metadata": {
        "collapsed": true
       },
       "outputs": [],
       "source": [
        "%cd ~/Dropbox/Data/\\n",
        "%run ./python/ipynb_startup.py"
       ]
      },

     '''

    nb_end =r'''
     ],
     "metadata": {
      "kernelspec": {
       "display_name": "Python [Root]",
       "language": "python",
       "name": "Python [Root]"
      },
      "language_info": {
       "codemirror_mode": {
        "name": "ipython",
        "version": 3
       },
       "file_extension": ".py",
       "mimetype": "text/x-python",
       "name": "python",
       "nbconvert_exporter": "python",
       "pygments_lexer": "ipython3",
       "version": "3.5.2"
      }
     },
     "nbformat": 4,
     "nbformat_minor": 0
    }'''

    code_start='\n'+r'''  {
       "cell_type": "code",
       "execution_count": null,
       "metadata": {
        "collapsed": true
       },
       "outputs": [],
       "source": [
       '''

    code_end=r'''
    ]
      },
    '''


    markdown_start='\n'+r'''  {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
    '''
    markdown_end=r'''
       ]
      },
    '''

    #infile=os.path.join('.','test','s3.py')
    with open(infile,'r') as f_in:
        fcontent = JSONEncoder().encode(f_in.read())
        cells=fcontent[1:-1].split(sep='#%%')
        nb_content=nb_start
        for string in cells[1:]:
            if string[0]=='#':
                lines=string[1:].strip('\\n').split(sep='\\n')
                this_cell=''
                for line in lines:
                    this_cell+='"'+line+'\\n",\n'
                this_cell=this_cell.rstrip(',\n')
                this_cell=this_cell[0:-3]+this_cell[-1]
                nb_content+=markdown_start+this_cell+markdown_end
            else:
                lines=string[2:].strip('\\n').split(sep='\\n')
                this_cell=''
                for line in lines:
                    this_cell+='"'+line+'\\n",\n'
                this_cell=this_cell.rstrip(',\n')
                this_cell=this_cell[0:-3]+this_cell[-1]
                nb_content+=code_start+this_cell+code_end

        nb_content=nb_content.rstrip()[:-1]
        nb_content+=nb_end
    #outfile=os.path.join('.','test','s3.ipynb')
    with open(outfile,'w') as f_out:
        f_out.write(nb_content)
