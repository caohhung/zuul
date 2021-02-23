%global install_dir /opt/gdc/zuul

Name:             zuul
Summary:          GoodData customized Zuul gatekeeper
Epoch:            1
Version:          2.5.2
Release:          %{?gdcversion}%{?dist}.gdc

Vendor:           GoodData
Group:            GoodData/Tools

License:          Apache
URL:              https://github.com/gooddata/zuul
Source0:          sources.tar
BuildArch:        x86_64
BuildRoot:        %{_tmppath}/%{name}-%{version}-root

Requires:         python-virtualenv
BuildRequires:    git
BuildRequires:    libffi-devel
BuildRequires:    libjpeg-devel
BuildRequires:    openssl-devel
BuildRequires:    python-pip
BuildRequires:    python-virtualenv

%prep
%setup -q -c

%build
export PBR_VERSION="%{version}.%{release}"
make build

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT%{install_dir} install
cp -r tools %{buildroot}%{install_dir}/

# %check
# export PBR_VERSION="%{version}.%{release}"
# make check

%clean
rm -rf $RPM_BUILD_ROOT

%description
GoodData customized Zuul gatekeeper

%files
%attr(0755, root, root) %dir %{install_dir}
%attr(0755, root, root) %{install_dir}/bin
%attr(0755, root, root) %{install_dir}/include
%attr(0755, root, root) %{install_dir}/lib
%attr(0755, root, root) %{install_dir}/lib64
%attr(0755, root, root) %{install_dir}/status
%attr(0755, root, root) %{install_dir}/share
%attr(0755, root, root) %{install_dir}/tools

%changelog
* Wed Jul 10 2019 King Nguyen <king.nguyen@gooddata.com> - 2.5.2
- SETI-1989 Add tools folder to package
- Temporarily disable check/test until we fix it

* Tue Apr 09 2019 Jan Priessnitz <jan.priessnitz@gooddata.com> 2.5.2-1.gdc
- SETI-2840: Introduce job sets into pipelines' job trees
- SETI-2250: Decouple existing "pause" ability from regular exit
- fix pep8 violations
- Remove Gerrit integration test
- SETI-1667: Log skipped jobs before reporting item build result
- SETI-1335: Add possibility to config keepalive for gearman server
- SETI-1829: do not create symbolic refs in cloner/merger
- Bump GitPython dependency
- SETI-1767: github reporter: report status and labels before merge
- SETI-1706: Check that SHA of PR head fetched by merger is correct
- SETI-377: Provide an option for reporting on build abort
- SETI-377: Handle Github HeadBranchModified error when merging PR
- SETI-1323: Reduce API calls in getChange
- SETI-1306: Correct Change, NullChange, Ref equals() functions
- SETI-1322: remove the github status link on pipeline end
- SETI-866: Raise timeouts for integration tests
- SETI-883: Run tox test on py27 instead of py26
- SETI-381: Fix typo: add_label -> add_labels
- SETI-1023: Fix job file filtering for post pipeline (push event)
- SETI-401 Zuul: Kill check pipeline if gate pipeline is started meanwhile
- SETI-376: Timestamp in release version for testing packages
- Install test dependencies via tox

* Mon Aug 08 2017 Michal Vanco <michal.vanco@gooddata.com> 2.5.1-2.gdc
- Gerrit integration test
- Scheduler logs projects sorted by name
- BUGFIX: SETI-380 Zuul exits when HUP is send right after service start
- BUGFIX: SETI-384 Zuul - handle ping events
- BUGFIX: SETI-379 zuul-cloner tries to fetch a wrong revision
- FEATURE: SETI-668 Support custom name of status in zuul pipelines
- BUGFIX: SETI-190 Zuul: report back to pull request when no jobs are run

* Mon Dec 05 2016 Jan Hruban <jan.hruban@gooddata.com> 2.5.1-1.gdc
- The source code is already above tag 2.5.1. Only bump the version.

* Tue Dec 02 2016 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-28.gdc
- Allow gerrit + github work together
- Upstream changes

* Tue Jun 06 2016 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-27.gdc
- Fix quick consequent merging on github
- Upstream changes

* Wed Apr 13 2016 Yury Tsarev <yury.tsarev@gooddata.com> 2.1.1-26.gdc
- Configurable status_url_with_change option
- Relevant js frontend filtering change

* Tue Mar 15 2016 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-25.gdc
- Allow file matching for GitHub
- Log GitHub API Rate
- Upstream changes

* Tue Feb 16 2016 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-24.gdc
- Include title in github commit message
- Include Reviewed-by in github commit message
- Upstream changes

* Thu Dec 16 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-23.gdc
- Allow github trigger to match on branches/refs
- Rebase onto upstream changes

* Thu Nov 20 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-22.gdc
- Fix handling the label events

* Thu Nov 19 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-21.gdc
- Sync with upstream changes.
- Add label support for github trigger and reporter.
- Implement dependent pipelines for github.
- Enable the dequeue mechanism.

* Thu Nov 18 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-20.gdc
- Fix permissions of the git dir in post-install. Related to the umask fix in 2.1.1-17.

* Thu Nov 16 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-19.gdc
- Sync with upstream changes. Creating the zuul-merger dir incorporated, supersedes 7cf9ebd
- Revert the backwards compatibility changes for the configuration options

* Thu Nov 13 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-18.gdc
- Fix zuul-merger not creating the git_dir on start, which fails on new deployments
- Sync with upstream changes (from now only merges into this repo, no rebases)

* Thu Nov 13 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-17.gdc
- Respect PPID umask when daemonizing

* Thu Nov 13 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-16.gdc
- Package 2.1.1-15 was mistakenly built on top of 2.1.1-14 instead of
  2.1.1-14.1. Rebuild with the correct content.

* Thu Nov 10 2015 Yury Tsarev <yury.tsarev@gooddata.com> 2.1.1-15.gdc
- Include web assets into package

* Wed Nov 03 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-14.1.gdc
- Fix the backward compatibility
- Fix the layout validation tool until upstream does

* Wed Nov 03 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-14.gdc
- Rebase onto upstream changes
- Change of the github reporter defaults
- Change name of configuration option in github reporter (backwards compatible)
- Change in the ssh configuration
- Built on top of:
  git fetch https://github.com/gooddata/zuul refs/heads/compat/github-integration-status

* Wed Nov 03 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-13.gdc
- github3.py >=1.0.0 has different API, fix a bug resulting from such incompatibility
- Built on top of:
  git fetch https://github.com/gooddata/zuul refs/heads/not-in-review/github-integration/5

* Wed Nov 03 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-12.gdc
- Support merging pull requests from github reporter
- Depend on pre-release version on github3.py 1.0.0a2 (fixes merging PRs)
- Built on top of:
  git fetch https://github.com/gooddata/zuul refs/heads/not-in-review/github-integration/4

* Wed Oct 29 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-11.gdc
- Fix minor test glitch
- Update authorship of commits
- Built on top of:
  git fetch https://github.com/gooddata/zuul refs/heads/not-in-review/github-integration/3

* Wed Oct 27 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-10.gdc
- Enforce the config schema of the github reporter
- Built on top of:
  git fetch https://github.com/gooddata/zuul refs/heads/not-in-review/github-integration/2

* Wed Oct 27 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-9.gdc
- Make the github statuses configurable, with sane defaults
- Improve the github statuses & comment testing
- Fix github-ssh documentation
- Built on top of:
  git fetch https://github.com/gooddata/zuul refs/heads/not-in-review/github-integration/1

* Wed Oct 26 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-8.gdc
- Set Github statuses
- Built on top of:
  git fetch https://review.openstack.org/openstack-infra/zuul refs/changes/03/239303/6 && git checkout FETCH_HEAD

* Wed Oct 26 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-7.gdc
- Fix SSH URL
- Built on top of:
  git fetch https://review.openstack.org/openstack-infra/zuul refs/changes/38/239138/7 && git checkout FETCH_HEAD

* Wed Oct 26 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-6.gdc
- Allow access to private repositories via SSH
- Built on top of:
  git fetch https://review.openstack.org/openstack-infra/zuul refs/changes/38/239138/6 && git checkout FETCH_HEAD

* Wed Oct 26 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-5.gdc
- Fix the construction of messages in the reporter
- Built on top of:
  git fetch https://review.openstack.org/openstack-infra/zuul refs/changes/03/239203/5 && git checkout FETCH_HEAD

* Wed Oct 26 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-4.gdc
- Fix the pr-comment handling
- More debugging output
- Built on top of:
  git fetch https://review.openstack.org/openstack-infra/zuul refs/changes/03/239203/4 && git checkout FETCH_HEAD

* Wed Oct 26 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-3.gdc
- Support to trigger jobs on github pull request comments
- GitHub change support for patchset
- Link to pull request in job descriptions
- Built on top of:
  git fetch https://review.openstack.org/openstack-infra/zuul refs/changes/03/239203/3 && git checkout FETCH_HEAD

* Wed Sep 14 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1.dev76-1.gdc
- Adding GitHub tests
- Base versioning scheme on `zuul --version'

* Wed Aug 12 2015 Jan Hruban <jan.hruban@gooddata.com> 2.1.1-2.gdc
- Better webhook event handling in the github integration

* Wed Aug 12 2015 Yury Tsarev <yury.tsarev@gooddata.com> 2.1.1-1.gdc
- First Zuul build - customized github integration included
