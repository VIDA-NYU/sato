import io
import os
from setuptools import setup


os.chdir(os.path.abspath(os.path.dirname(__file__)))


req = [
    'gensim',
    'nltk',
    'numpy',
    'pandas',
    'python-dateutil',
    'scikit-learn',
    'scipy',
    'tqdm',
    'torch',
    'ConfigArgParse',
    'tensorboardX',
]
with io.open('README.rst', encoding='utf-8') as fp:
    description = fp.read()
setup(name='sato',
      version='0.1',
      packages=[
          'sato', 'sato.model', 'sato.model.torchcrf', 'sato.extract',
          'sato.topic_model', 'sherlock', 'sherlock.features',
      ],
      package_data={
          'sato': [
              'configs/feature_groups/char_col.tsv',
              'configs/feature_groups/par_col.tsv',
              'configs/feature_groups/rest_col.tsv',
              'configs/feature_groups/word_col.tsv',
              'configs/types.json',
              'demo/pretrained_sato/model.pt',
          ],
          'sato.topic_model': [
              'LDA_cache/type78/dictionary_num-directstr_thr-0_tn-400',
              'LDA_cache/type78/model_num-directstr_thr-0_tn-400',
              'LDA_cache/type78/model_num-directstr_thr-0_tn-400.expElogbeta.npy',
              'LDA_cache/type78/model_num-directstr_thr-0_tn-400.id2word',
              'LDA_cache/type78/model_num-directstr_thr-0_tn-400.state',
              'LDA_cache/type78/model_num-directstr_thr-0_tn-400.state.sstats.npy',
          ],
          'sherlock': [
              'pretrained/glove.6B/glove.6B.50d.txt',
              'pretrained/par_vec_trained_400.pkl',
              'pretrained/par_vec_trained_400.pkl.docvecs.vectors_docs.npy',
          ],
      },
      install_requires=req,
      description="Contextual Semantic Type Detection in Tables",
      author="Dan Zhang, Yoshihiko Suhara, Jinfeng Li, Madelon Hulsebos, Çağatay Demiralp, Wang-Chiew Tan",
      maintainer="Remi Rampin",
      maintainer_email='remi.rampin@nyu.edu',
      url='https://gitlab.com/ViDA-NYU/datamart/sato',
      project_urls={
          'Homepage': 'https://gitlab.com/ViDA-NYU/datamart/sato',
          'Source': 'https://gitlab.com/ViDA-NYU/datamart/sato',
          'Tracker': 'https://gitlab.com/ViDA-NYU/datamart/sato/issues',
      },
      long_description=description,
      license='Apache-2.0',
      keywords=['sato', 'type', 'semantic', 'table', 'data'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Scientific/Engineering :: Information Analysis'])
