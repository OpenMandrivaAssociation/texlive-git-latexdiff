Name:		texlive-git-latexdiff
Version:	54732
Release:	1
Summary:	Call latexdiff on two Git revisions of a file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/git-latexdiff
License:	bsd2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/git-latexdiff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/git-latexdiff.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
git-latexdiff is a tool to graphically visualize differences
between different versions of a LaTeX file. Technically, it is
a wrapper around git and latexdiff.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/git-latexdiff
%doc %{_texmfdistdir}/texmf-dist/doc/support/git-latexdiff
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/git-latexdiff.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/git-latexdiff.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
