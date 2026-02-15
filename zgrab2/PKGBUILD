# Maintainer:  Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=zgrab2
pkgver=1.0.0
pkgrel=1
pkgdesc="Fast Application Layer Scanner"
arch=(x86_64)
url=https://github.com/zmap/zgrab2
license=(Apache-2.0)
depends=(glibc)
makedepends=(
    git
    go
)
source=($pkgname::git+https://github.com/zmap/zgrab2#tag=v$pkgver)
b2sums=('e1f158eed9cf0199396c47257d8a99d6407f2afc8690cc62a307236e5b1e9bf759cdd4ec16a16f056ec9908cd0b6b4b039a720df09046ee429e59e817eaf5123')
options=(!lto)

prepare(){
    cd $pkgname
    mkdir -p build
}

build() {
    cd $pkgname
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
    go build -o build ./cmd/...
}

check() {
    cd $pkgname
    # Test currently only runs on the modules folder because some of the
    # third-party libraries in lib (e.g. http) are failing.
    # See https://github.com/zmap/zgrab2/blob/062ec5e6030e214da480a056105e95be1a0fd18f/Makefile#L17
    go test -v -failfast .
    cd lib/output/test && go test -v -failfast ./...
    cd "$srcdir"/$pkgname/modules && go test -v -failfast ./...
}

package() {
    cd $pkgname
    install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
    install -D -m755 build/zgrab2 "$pkgdir"/usr/bin/zgrab2
}
