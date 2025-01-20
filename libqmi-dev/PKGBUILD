# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
pkgname=(
  libqmi-dev
  libqmi-dev-docs
)
pkgver=1.35.6_dev
pkgrel=1
pkgdesc="QMI modem protocol helper library"
url="https://www.freedesktop.org/wiki/Software/libqmi/"
arch=(x86_64)
license=('GPL-2.0-or-later AND LGPL-2.1-or-later')
depends=(
  bash
  gcc-libs
  glib2
  glibc
  libgudev
  libmbim
  libqrtr-glib
)
makedepends=(
  bash-completion
  git
  gobject-introspection
  gtk-doc
  help2man
  meson
)
source=(git+https://gitlab.freedesktop.org/mobile-broadband/libqmi.git?signed#tag=${pkgver//_/-})
b2sums=('59ce626f4d519e6117202450186d0252dfafbd9333cecf27864c8a3bb4caee97e3f7e2934e0d1c2df82d9092349bc14eea8956b4d80d62efe4e9b9973753789f')
validpgpkeys=(
  A814D09B9C5BC01945A64308AECE0239C6606AD5 # Aleksander Morgado <aleksandermj@chromium.org>
)

build() {
  local meson_options=(
    -D gtk_doc=true
  )

  arch-meson libqmi build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs --no-rebuild
}

package_libqmi-dev() {
  provides=(libqmi libqmi-glib.so)
  conflicts=(libqmi)

  meson install -C build --destdir "$pkgdir" --no-rebuild

  mkdir -p doc/usr/share
  mv {"$pkgdir",doc}/usr/share/gtk-doc
}

package_libqmi-dev-docs() {
  pkgdesc+=" (documentation)"
  depends=()
  provides=(libqmi-docs)
  conflicts=(libqmi-docs)

  mv doc/* "$pkgdir"
}

# vim:set sw=2 sts=-1 et:
