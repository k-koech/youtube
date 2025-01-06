"use client"
import Image from 'next/image'
import Link from 'next/link'
import React, {useState, useEffect} from 'react'

export default function Blog() 
{

  const [posts, setPosts] = useState(null)
 
  useEffect(() => {
    async function fetchPosts() {
      const res = await fetch('http://localhost:3000/blogs')
      const data = await res.json()
      setPosts(data)
    }
    fetchPosts()
  }, [])
 
  if (!posts) return <div>Loading...</div>


  return (
    <div>
        <h1>Blog</h1>
        <div className="grid grid-cols-2 md:grid-cols-4">
        {
            posts.map((post, index) => (
                <Link href={`blog/${post.id}`}  key={index}>
                    <div className="border p-4 m-6">
                      <Image src={post.image} alt={post.title} width={200} height={200} layout="responsive" />
                      <h2>{post.title}</h2>
                      <p>{post.content}</p>
                    </div>
                </Link>
            ))
        }
        </div>
    </div>
  )
}
