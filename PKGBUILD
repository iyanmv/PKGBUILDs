# Maintainer: Frederic Van Assche <frederic@fredericva.com>

pkgname=python-influxdb-client
pkgver=1.41.0
pkgrel=1
pkgdesc="Python client for InfluxDB 1.8+ and 2.0"
arch=('any')
url="https://github.com/influxdata/influxdb-client-python/"
license=('MIT')
depends=('python>=3.7' 'python-dateutil>=2.5.3' 'python-reactivex>=4.0.4' 'python-certifi>=14.05.14' 'python-urllib3>=1.26.0')
makedepends=('python-setuptools>=21.0.0')
optdepends=('influxdb' 'python-ciso8601>=2.1.1' 'python-pandas>=1.0.0' 'python-numpy' 'python-aiohttp>=3.8.1' 'python-aiocsv>=1.2.2')
options=(!emptydirs)
source=($pkgname-$pkgver.tar.gz::https://github.com/influxdata/influxdb-client-python/archive/v$pkgver.tar.gz)
sha512sums=('cfc95626106cd45fd6376781962cd852c138851ac4761267df22231e54b0a589b6572a06e3fb89012eecdc93c0c7860d6e84285cc785b1baa62f411979cefbe9')

build() {
  cd "$srcdir/influxdb-client-python-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/influxdb-client-python-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
