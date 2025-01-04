import Link from 'next/link'
import React from 'react'

export default function Blog() {
    const posts = [
    {
      title: "Hello World",
      content: "Hello World from Next.js"
    },
    {
      title: "Second Post",
      content: "This is my  second post"
    }]

  return (
    <div>
        <h1>Blog</h1>
        {
            posts.map((post, index) => (
                <Link href={`blog/${post.title}`}  key={index}>
                    <div className="border p-4 m-6">
                    <h2>{post.title}</h2>
                    <p>{post.content}</p>
                    </div>
                </Link>
            ))
        }
    </div>
  )
}
