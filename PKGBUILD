# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=xmss
_name=xmss-reference
_commit=171ccbd26f098542a67eb5d2b128281c80bd71a6
pkgver=r136.171ccbd
pkgrel=1
pkgdesc="XMSS (eXtended Merkle Signature Scheme) reference code (RFC 8391)"
arch=(x86_64)
url=https://github.com/XMSS/xmss-reference
license=(Unlicense)
depends=(openssl)
makedepends=(
    git
    wolfssl-liboqs
)
source=(
    $_name::git+$url#commit=$_commit
    xmss-wolfssl.patch::https://raw.githubusercontent.com/wolfSSL/wolfssl-examples/master/pq/stateful_hash_sig/0001-Patch-to-support-wolfSSL-xmss-reference-integration.patch
)
b2sums=('1f9c0cc684bcf2ad1a7ef3e43cf8239d09b3e39065ead002b8440c382a43f80d99379fb576bbbebc82859afce262591a5b022eb342bc00acec7bc2c8b406ef6b'
        'bc390e6226419be1a5919800fde00d6ed704a323549921f50971c0d0cfe8057007b06eebe0483a5e1fdc494fe9c284da7242cb82f43a9738b862273b1663fad6')

pkgver() {
    cd $_name
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

prepare() {
    # https://github.com/wolfSSL/wolfssl-examples/tree/master/pq/stateful_hash_sig
    git apply --directory=$_name xmss-wolfssl.patch
}

build() {
    cd $_name
    make all
}

#check () {
#    cd $_name
#    for test in $(find ./test -type f -executable); do
#        ./$test
#    done
#}

package() {
    cd $_name
    install -d "$pkgdir"/usr/bin
    for exec in $(find ./ui -type f -executable); do
        install -vDm 755 $exec "$pkgdir"/usr/bin
    done
}

