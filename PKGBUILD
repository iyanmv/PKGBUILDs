# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=openqasm
pkgname=python-${_pkgname}3
pkgver=1.0.0
pkgrel=1
pkgdesc="Reference OpenQASM AST in Python"
arch=(any)
url=https://github.com/openqasm/openqasm
license=(Apache-2.0)
conflicts=(python-qiskit-terra)
depends=(
    python-antlr4
    python-importlib-metadata
)
makedepends=(
    antlr4
    git
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(python-pytest)
source=($_pkgname::git+https://github.com/openqasm/openqasm#tag=ast-py/v$pkgver)
b2sums=('ff614b9b484a3f275125316255f9b82c31e620b81ab9f8d21762a0841172afdd99872039ba8fdfa74eca6af459c415f88d2f93431b457876316c1fdfc8bf2884')

build() {
    cd $_pkgname/source/grammar

    # Build the ANTLR files
    local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
    local antlr_version=$(ls /usr/share/java/antlr-*-complete.jar | cut -d "-" -f 2)
    local antlr_major=$(echo $antlr_version | cut -d "." -f 1)
    local antlr_minor=$(echo $antlr_version | cut -d "." -f 2)
    local antlr_out_dir=../$_pkgname/${_pkgname}3/_antlr/_${antlr_major}_${antlr_minor}
    mkdir -p $antlr_out_dir
    java -Xmx500M -jar /usr/share/java/antlr-complete.jar -o $antlr_out_dir -Dlanguage=Python3 -visitor qasm3Lexer.g4 qasm3Parser.g4

    # Build the wheel package
    cd ../$_pkgname
    python -m build --wheel --no-isolation
}

check() {
   cd $_pkgname/source/$_pkgname
   local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
   python -m installer --destdir=../test_dir dist/*.whl
   # Delete folder in src to be sure we test with installed package
   rm -r ${_pkgname}3
   PYTHONPATH=../test_dir/$_site_packages pytest tests
}

package() {
    cd $_pkgname/source/$_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
