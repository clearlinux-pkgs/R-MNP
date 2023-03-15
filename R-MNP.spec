#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MNP
Version  : 3.1.4
Release  : 40
URL      : https://cran.r-project.org/src/contrib/MNP_3.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MNP_3.1-4.tar.gz
Summary  : Fitting the Multinomial Probit Model
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-MNP-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
 developed by Imai and van Dyk (2005). "A Bayesian Analysis of the 
 Multinomial Probit Model Using the Data Augmentation." Journal of 
 Econometrics, Vol. 124, No. 2 (February), pp. 311-334.

%package lib
Summary: lib components for the R-MNP package.
Group: Libraries

%description lib
lib components for the R-MNP package.


%prep
%setup -q -n MNP
cd %{_builddir}/MNP

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678894713

%install
export SOURCE_DATE_EPOCH=1678894713
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/MNP/tests/testthat.R
/usr/lib64/R/library/MNP/tests/testthat/test-all.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/MNP/libs/MNP.so
/usr/lib64/R/library/MNP/libs/MNP.so.avx2
/usr/lib64/R/library/MNP/libs/MNP.so.avx512
