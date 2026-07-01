# Deployment Checklist

Use this checklist before deploying to production.

## Pre-Deployment

- [ ] **API Key Setup**
  - [ ] OpenAI API key created and verified
  - [ ] Account has available API credits
  - [ ] Key is stored securely (never in code)

- [ ] **Code Review**
  - [ ] All changes committed and pushed
  - [ ] No console.log or debug statements
  - [ ] No hardcoded secrets in code
  - [ ] TypeScript types are correct
  - [ ] No unused imports or variables

- [ ] **Testing**
  - [ ] Run locally: `npm run dev`
  - [ ] Test chat functionality in browser
  - [ ] Test message sending and receiving
  - [ ] Test error handling (invalid API key, network issues)
  - [ ] Check responsive design on mobile
  - [ ] Build locally: `npm run build` (succeeds without errors)

- [ ] **Dependencies**
  - [ ] All required packages in package.json
  - [ ] No security vulnerabilities: `npm audit`
  - [ ] No unused dependencies
  - [ ] Lock file (package-lock.json) committed

## Configuration Review

- [ ] **Environment Variables**
  - [ ] `.env.example` up to date with all required vars
  - [ ] `.env.local` has correct values (local only)
  - [ ] No sensitive data in version control
  - [ ] Vercel environment variables configured

- [ ] **Next.js Configuration**
  - [ ] `next.config.mjs` optimized for production
  - [ ] Build errors resolved (no `ignoreBuildErrors: true`)
  - [ ] Image optimization enabled
  - [ ] TypeScript strict mode enabled

- [ ] **Vercel Configuration**
  - [ ] `vercel.json` present and correct
  - [ ] Build command specified
  - [ ] Environment variables listed
  - [ ] Regions configured appropriately

## Deployment Process

- [ ] **Initial Deployment to Vercel**
  1. [ ] Connect GitHub repository to Vercel
  2. [ ] Select correct branch (deploy-project or main)
  3. [ ] Add environment variables in Vercel dashboard
  4. [ ] Trigger deployment
  5. [ ] Wait for build to complete

- [ ] **Post-Deployment Testing**
  - [ ] Deployment successful in Vercel dashboard
  - [ ] Application loads at deployment URL
  - [ ] Chat functionality works end-to-end
  - [ ] No errors in Vercel logs
  - [ ] Response times are acceptable

- [ ] **Monitoring Setup**
  - [ ] Enable Vercel Analytics
  - [ ] Set up error tracking if needed
  - [ ] Monitor API usage
  - [ ] Set up alerts for errors/outages

## Post-Deployment

- [ ] **Verification**
  - [ ] Test all features on production
  - [ ] Check Core Web Vitals in Vercel Analytics
  - [ ] Verify API responses are working
  - [ ] Confirm user experience is smooth

- [ ] **Documentation**
  - [ ] Update README with production URL
  - [ ] Document any deployment-specific configurations
  - [ ] Add to team documentation if applicable
  - [ ] Create deployment runbook for future reference

- [ ] **Maintenance**
  - [ ] Set up regular monitoring
  - [ ] Plan for dependency updates
  - [ ] Document rollback procedure
  - [ ] Schedule security audits

## Common Issues

### Build Failures
```bash
# Clear cache and rebuild
vercel env list
vercel redeploy
```

### API Key Not Working
1. Verify key in Vercel Environment Variables
2. Check OpenAI API status
3. Confirm account has credits
4. Redeploy after fixing

### Module Not Found Errors
1. Check package.json dependencies
2. Ensure lock file is committed
3. Verify build log for missing packages

### Performance Issues
1. Check response times in Analytics
2. Monitor API usage
3. Consider caching strategies
4. Review Vercel function logs

## Rollback Plan

If deployment has issues:

1. **Quick Rollback** (Last deployment)
   - Vercel Dashboard → Deployments
   - Select previous version → "Promote to Production"

2. **Full Rollback** (To main branch)
   - Roll back GitHub branch
   - Create new pull request
   - Deploy from stable version

3. **Hotfix Deployment**
   - Create hotfix branch from main
   - Fix issue locally
   - Test thoroughly
   - Deploy hotfix branch
   - Merge back to main

## Support Resources

- **Vercel Dashboard**: https://vercel.com/dashboard
- **Vercel Docs**: https://vercel.com/docs
- **OpenAI Status**: https://status.openai.com
- **GitHub Issues**: Check repository issues
- **Discord Community**: Vercel community support

## Sign-Off

- [ ] Deployment reviewed by team lead
- [ ] All checks passed
- [ ] Production environment verified
- [ ] Monitoring confirmed working
- [ ] Team notified of deployment

---

**Deployed by**: [Your Name]  
**Date**: [Deployment Date]  
**Version**: [Git Commit Hash]  
**Status**: ✅ Production Ready / ⚠️ Issues Found
