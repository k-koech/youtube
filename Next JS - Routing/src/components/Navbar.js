import Link from 'next/link'
import React from 'react'

export default function Navbar() {
  return (
<nav class="font-sans flex flex-col text-center sm:flex-row sm:text-left sm:justify-between py-4 px-6 bg-white shadow sm:items-baseline w-full">
  <div class="mb-2 sm:mb-0">
    <a href="#" class="text-2xl no-underline text-grey-darkest hover:text-blue-dark">Home</a>
  </div>
  <div>
    <Link href="/" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Home</Link>
    <Link href="/blog" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Blog</Link>
    <Link href="/contact" class="text-lg no-underline text-grey-darkest hover:text-blue-dark ml-2">Contact</Link>
  </div>
</nav>
  )
}
