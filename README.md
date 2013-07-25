GitHub User or Organization Pages update tool
=============================================

GitHub User or Organization Pages require a dedicated repository based on the account name (see [GitHub Pages documentation][doc]).
In order to let update your User or Organization Pages easily, `ghp-update` performs the following actions :

  * Clones your Pages repository to a temporary folder
  * Replaces the repository content with the new content you want to publish
  * Commits and pushes all changes

[doc]: https://help.github.com/articles/user-organization-and-project-pages "User, Organization and Project Pages - GitHub Help"

Install
-------

    pip install ghp-update

Usage
-----

    Usage: ghp-update [-m "Custom commit message"] CONTENT_DIR GIT_REPOSITORY_URL
    
    Options:
      -m MESSAGE  The commit message to use when adding the new content
      -h, --help  show this help message and exit

`ghp-update` deletes all repository contents before copying the new content to your repository.

You can specify a custom commit message by using the `-m` option.

License
-------

`ghp-update` is distributed under the GNU GENERAL PUBLIC LICENSE version 2. See the LICENSE file for more information

Thanks
------

`ghp-update` has been inspired by the [ghp-import][ghp-import] utility !

[ghp-import]: http://github.com/davisp/ghp-import/ "Easily import docs to your gh-pages branch"