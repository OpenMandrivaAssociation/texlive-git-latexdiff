%global tl_name git-latexdiff
%global tl_revision 75878
%global tl_bin_links git-latexdiff:%{_texmfdistdir}/scripts/git-latexdiff/git-latexdiff

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7.1
Release:	%{tl_revision}.1
Summary:	Call latexdiff on two Git revisions of a file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/git-latexdiff
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/git-latexdiff.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/git-latexdiff.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(git-latexdiff.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
git-latexdiff is a tool to graphically visualize differences between
different versions of a LaTeX file. Technically, it is a wrapper around
git and latexdiff.

