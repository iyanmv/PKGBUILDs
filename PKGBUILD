# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=http-relay
pkgname=drand-$_pkgname
pkgver=2.1.0
pkgrel=1
pkgdesc="An HTTP relay for drand nodes"
arch=(x86_64)
url=https://github.com/drand/http-relay
license=('Apache-2.0 OR MIT')
depends=(glibc)
makedepends=(
    git
    go
)
source=($_pkgname::git+https://github.com/drand/http-relay.git#tag=v$pkgver)
b2sums=('fd4efec48e39b2ce29338a6ffb5efae594c1d36be17ae4895c7134dab92130e435e91616be01e8a0d0ce68cf2bb36f1bae79654eb0ce528aea54c183f9e96365')

build() {
    cd $_pkgname
    mkdir -p build
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
    go build -o build
}

package() {
    cd $_pkgname
    install -Dm755 build/$_pkgname "$pkgdir"/usr/bin/$pkgname
    install -Dm644 LICENSE-MIT "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
