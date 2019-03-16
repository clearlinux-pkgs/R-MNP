#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MNP
Version  : 3.1.0
Release  : 6
URL      : https://cran.r-project.org/src/contrib/MNP_3.1-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MNP_3.1-0.tar.gz
Summary  : R Package for Fitting the Multinomial Probit Model
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-MNP-lib
BuildRequires : clr-R-helpers

%description
Monte Carlo.  The multinomial probit model is often used to analyze 
 the discrete choices made by individuals recorded in survey data. 
 Examples where the multinomial probit model may be useful include the 
 analysis of product choice by consumers in market research and the 
 analysis of candidate or party choice by voters in electoral studies.  
 The MNP package can also fit the model with different choice sets for 
 each individual, and complete or partial individual choice orderings 
 of the available alternatives from the choice set. The estimation is
 based on the efficient marginal data augmentation algorithm that is 
 developed by Imai and van Dyk (2005). ``A Bayesian Analysis of the 
 Multinomial Probit Model Using the Data Augmentation,'' Journal of 
 Econometrics, Vol. 124, No. 2 (February), pp. 311-334.

%package lib
Summary: lib components for the R-MNP package.
Group: Libraries

%description lib
lib components for the R-MNP package.


%prep
%setup -q -c -n MNP

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530426565

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530426565
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MNP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MNP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MNP
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library MNP|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MNP/DESCRIPTION
/usr/lib64/R/library/MNP/INDEX
/usr/lib64/R/library/MNP/Meta/Rd.rds
/usr/lib64/R/library/MNP/Meta/data.rds
/usr/lib64/R/library/MNP/Meta/features.rds
/usr/lib64/R/library/MNP/Meta/hsearch.rds
/usr/lib64/R/library/MNP/Meta/links.rds
/usr/lib64/R/library/MNP/Meta/nsInfo.rds
/usr/lib64/R/library/MNP/Meta/package.rds
/usr/lib64/R/library/MNP/Meta/vignette.rds
/usr/lib64/R/library/MNP/NAMESPACE
/usr/lib64/R/library/MNP/R/MNP
/usr/lib64/R/library/MNP/R/MNP.rdb
/usr/lib64/R/library/MNP/R/MNP.rdx
/usr/lib64/R/library/MNP/data/Rdata.rdb
/usr/lib64/R/library/MNP/data/Rdata.rds
/usr/lib64/R/library/MNP/data/Rdata.rdx
/usr/lib64/R/library/MNP/doc/MNP.Rnw
/usr/lib64/R/library/MNP/doc/MNP.pdf
/usr/lib64/R/library/MNP/doc/index.html
/usr/lib64/R/library/MNP/help/AnIndex
/usr/lib64/R/library/MNP/help/MNP.rdb
/usr/lib64/R/library/MNP/help/MNP.rdx
/usr/lib64/R/library/MNP/help/aliases.rds
/usr/lib64/R/library/MNP/help/paths.rds
/usr/lib64/R/library/MNP/html/00Index.html
/usr/lib64/R/library/MNP/html/R.css
/usr/lib64/R/library/MNP/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/MNP/libs/MNP.so
/usr/lib64/R/library/MNP/libs/MNP.so.avx2
/usr/lib64/R/library/MNP/libs/MNP.so.avx512
