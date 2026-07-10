%global tl_name broydensolve
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Solve a system of equations with Broydens good method
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/broydensolve
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/broydensolve.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/broydensolve.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements Broyden's good method to solve a system of
equations. It is also possible to use coordinates defined by TikZ as
known and unknown variables.

