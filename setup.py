from distutils.core import setup
setup(
  name = 'shrtcode',
  packages = ['shrtcode'],
  version = '0.1',
  license='MIT',
  description = 'A wrapper for the Shrtcode API made in python',
  author = 'Yukari-san',
  author_email = 'luiz2005eduardo@gmail.com',
  url = 'https://github.com/Yukari-san/shrtcode-api-wrapper/',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['wrapper', 'shrtcode', 'url_shortener', 'no_authentication'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7,
    'Programming Language :: Python :: 3.8,
    'Programming Language :: Python :: 3.9,
  ],
)
