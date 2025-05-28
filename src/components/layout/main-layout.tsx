import * as React from 'react';
import { motion } from 'framer-motion';
import { useTheme } from 'next-themes';
import { Button } from '@/components/ui/button';
import { Sun, Moon } from 'lucide-react';

interface MainLayoutProps {
  children: React.ReactNode;
}

const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.4 } },
};

export function MainLayout({ children }: MainLayoutProps) {
  const { theme, setTheme } = useTheme();

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      <motion.header
        initial="hidden"
        animate="visible"
        variants={fadeIn}
        className="sticky top-0 z-40 w-full border-b border-gray-200 bg-white/50 backdrop-blur-xl dark:border-gray-800 dark:bg-gray-900/50"
      >
        <div className="container mx-auto flex h-16 items-center justify-between px-4">
          <div className="flex items-center gap-6">
            <a href="/" className="flex items-center space-x-2">
              <span className="text-2xl font-bold text-gray-900 dark:text-white">
                RecruitMate
              </span>
              <span className="rounded-md bg-primary-500 px-2 py-1 text-sm text-white">
                AI
              </span>
            </a>
            <nav className="hidden md:flex md:gap-6">
              <a
                href="/dashboard"
                className="text-sm font-medium text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
              >
                Dashboard
              </a>
              <a
                href="/candidates"
                className="text-sm font-medium text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
              >
                Candidates
              </a>
              <a
                href="/jobs"
                className="text-sm font-medium text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
              >
                Jobs
              </a>
            </nav>
          </div>
          <div className="flex items-center gap-4">
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            >
              {theme === 'dark' ? (
                <Sun className="h-5 w-5" />
              ) : (
                <Moon className="h-5 w-5" />
              )}
              <span className="sr-only">Toggle theme</span>
            </Button>
          </div>
        </div>
      </motion.header>

      <motion.main
        initial="hidden"
        animate="visible"
        variants={fadeIn}
        className="container mx-auto min-h-[calc(100vh-4rem)] px-4 py-8"
      >
        {children}
      </motion.main>

      <motion.footer
        initial="hidden"
        animate="visible"
        variants={fadeIn}
        className="border-t border-gray-200 bg-white py-8 dark:border-gray-800 dark:bg-gray-900"
      >
        <div className="container mx-auto px-4">
          <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
            <p className="text-center text-sm text-gray-500 dark:text-gray-400">
              © {new Date().getFullYear()} RecruitMate AI. All rights reserved.
            </p>
            <div className="flex gap-4">
              <a
                href="/privacy"
                className="text-sm text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
              >
                Privacy Policy
              </a>
              <a
                href="/terms"
                className="text-sm text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
              >
                Terms of Service
              </a>
            </div>
          </div>
        </div>
      </motion.footer>
    </div>
  );
}

export function ContentSection({ children, className }: MainLayoutProps) {
  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.2 }}
      className={cn(
        "rounded-2xl bg-card p-6 shadow-lg backdrop-blur-sm",
        "border border-border/50",
        "dark:bg-card/80",
        className
      )}
    >
      {children}
    </motion.section>
  );
}

export function PageHeader({
  title,
  description,
  className,
}: {
  title: string;
  description?: string;
  className?: string;
}) {
  return (
    <div className={cn("space-y-2", className)}>
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl"
      >
        {title}
      </motion.h1>
      {description && (
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="text-lg text-muted-foreground"
        >
          {description}
        </motion.p>
      )}
    </div>
  );
} 